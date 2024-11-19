import json
import shutil
import pathlib
import functools
import subprocess
import collections

from cldfbench import Dataset as BaseDataset
from cldfgeojson import aggregate
from pycountry import languages
from shapely.geometry import shape, Polygon, MultiPolygon, GeometryCollection, LineString, MultiLineString, Point
from shapely import distance, to_geojson, simplify
from shapely.validation import explain_validity, make_valid
from clldutils.jsonlib import dump
from csvw.dsv import UnicodeWriter
from cldfgeojson.create import merged_geometry


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "asher2007world"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return super().cldf_specs()

    def cmd_download(self, args):
        sdir = self.dir.parent / 'glottography-data' / 'worldatlas'
        shutil.copy(sdir / 'source' / '{}.bib'.format(sdir.name), self.raw_dir / 'sources.bib')
        # We want a valid geopackage:
        subprocess.check_call([
            'ogr2ogr',
            str(self.raw_dir / 'dataset.gpkg'),
            str(sdir / '{}.gpkg'.format(sdir.name)),
            '-makevalid',
            '-nlt', 'PROMOTE_TO_MULTI',
        ])
        subprocess.check_call([
            'ogr2ogr',
            str(self.raw_dir / 'dataset.geojson'),
            str(self.raw_dir / 'dataset.gpkg'),
            '-t_srs', 'EPSG:4326',
            '-s_srs', 'EPSG:3857',
        ])

    @functools.cached_property
    def poly2gc(self):
        res = collections.defaultdict(list)
        for row in self.etc_dir.read_csv('polygons.csv', dicts=True):
            res[row['name']].append((
                Point(float(row['lon']), float(row['lat'])),
                row['glottocode']))
        return res

    def iter_polys(self):
        i = 0
        invalid, polys, shapes = 0, [], []
        old, new, removed, weird = [], [], [], []
        maps = set()
        for f in self.raw_dir.read_json('dataset.geojson')['features']:
            if 'Contemporary' in f['properties']['map_name_full']:
                continue  # FIXME: Handle those, too!
            maps.add(f['properties']['map_name_full'])
            obj = shape(f['geometry'])
            if not obj.is_valid:
                invalid += 1
                old.append(f)
                obj = make_valid(obj)
                if isinstance(obj, GeometryCollection):
                    if (isinstance(obj.geoms[0], (MultiPolygon, Polygon))
                            and isinstance(obj.geoms[1], (LineString, MultiLineString))):
                        # Something sticking out. We drop the LineString.
                        removed.append(dict(type='Feature', geometry=json.loads(to_geojson(obj.geoms[1]))))
                        obj = obj.geoms[0]
                    else:
                        raise ValueError

                if not obj.is_valid:
                    raise ValueError
                    print(explain_validity(obj))

                new.append(dict(type='Feature', geometry=json.loads(to_geojson(obj))))

            if isinstance(obj, Polygon):
                obj = MultiPolygon([obj])

            #shapes.append(json.loads(to_geojson(simplify(obj, 0.5))))
            assert isinstance(obj, MultiPolygon), obj
            assert obj.is_valid

            for poly in obj.geoms:
                #
                # FIXME: possibly update metadata!
                #
                cent = poly.representative_point()
                if not poly.contains(cent):
                    # ignore these mini polygons.
                    assert poly.area < 1.1473590666151532e-17
                else:
                    polys.append([f['properties']['name'], f['properties']['glottocode'], cent.x, cent.y])

                for point, code in self.poly2gc.get(f['properties']['name'], []):
                    if poly.contains(point):
                        gc = code
                        break
                else:
                    gc = f['properties']['glottocode']
                if gc:
                    i += 1
                    yield (
                        i,
                        dict(
                            type='Feature',
                            properties=f['properties'],
                            geometry=json.loads(to_geojson(poly))),
                        gc)

                #except AssertionError:
                #    print(distance(poly, cent))
        #dump(dict(features=removed, type='FeatureCollection'), self.dir / 'removed.geojson')
        #dump(dict(features=old, type='FeatureCollection'), self.dir / 'tofix.geojson')
        #dump(dict(features=new, type='FeatureCollection'), self.dir / 'fixed.geojson')
        #dump(dict(features=[dict(type='Feature', geometry=merged_geometry(shapes))], type='FeatureCollection'), self.dir / 'all.geojson')
        #with UnicodeWriter(self.etc_dir / 'polygons.csv') as csvfile:
        #    csvfile.writerow(['name', 'glottocode', 'lon', 'lat'])
        #    csvfile.writerows(polys)

        #for n in sorted(maps, key=lambda x: int(x.split()[1])):
        #    print(n)

    def cmd_makecldf(self, args):
        """
        Convert the raw data to a CLDF dataset.

        >>> args.writer.objects['LanguageTable'].append(...)
        """
        from cldfgeojson import MEDIA_TYPE
        from cldfgeojson.create import aggregate

        args.writer.cldf.add_component('MediaTable')
        args.writer.cldf.add_component(
            'LanguageTable',
            {
                'name': 'Speaker_Area',
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#speakerArea'
            })

        features, languages = aggregate(list(self.iter_polys()), args.glottolog.api)
        #
        # FIXME: split geojson in per-family files?!
        #
        dump(dict(type='FeatureCollection', features=features), self.cldf_dir / 'languages.geojson')

        for (glang, pids, family), f in zip(languages, features):
            if 1:#lids is None or (glang.id not in lids):  # Don't append isolates twice!
                args.writer.objects['LanguageTable'].append(dict(
                    ID=glang.id,
                    Name=glang.name,
                    Glottocode=glang.id,
                    Latitude=glang.latitude,
                    Longitude=glang.longitude,
                    #Contribution_IDs=pids,
                    Speaker_Area='languages',
                    #Glottolog_Languoid_Level=ptype,
                    #Family=family,
                ))
        args.writer.objects['MediaTable'].append(dict(
            ID='languages',
            Name='Speaker areas for languages',
            Description='Speaker areas aggregated for Glottolog {}-level languoids, '
                        'color-coded by family.'.format('language'),
            Media_Type=MEDIA_TYPE,
            Download_URL='languages.geojson',
        ))

        return
        for lg, _, _ in languoids:
            args.writer.objects['LanguageTable'].append(dict(ID=lg.id, Name=lg.name, Glottocode=lg.id))





        features, languoids = aggregate(list(self.iter_polys()), args.glottolog.api, level='family')
        print(len(languoids))
        dump(dict(type='FeatureCollection', features=features), self.cldf_dir / 'families.json')
        #for lg, _, _ in languoids:
        #    args.writer.objects['LanguageTable'].append(dict(ID=lg.id, Name=lg.name, Glottocode=lg.id))
