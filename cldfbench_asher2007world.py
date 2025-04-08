import json
import pathlib
import itertools
import collections

import cldfbench
from shapely import intersection_all
from cldfgeojson import MEDIA_TYPE, aggregate, feature_collection
from cldfgeojson.geojson import dump
from clldutils.jsonlib import dump
from clldutils.markup import add_markdown_text
from pycldf.sources import Sources

import pyglottography
from pyglottography.dataset import Feature


class Dataset(pyglottography.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "asher2007world"

    def cldf_specs(self):
        return {
            'traditional': cldfbench.CLDFSpec(
                metadata_fname='traditional-metadata.json',
                dir=self.cldf_dir / 'traditional',
                module='Generic',
                writer_cls=cldfbench.CLDFWriter,
            ),
            'contemporary': cldfbench.CLDFSpec(
                metadata_fname='contemporary-metadata.json',
                dir=self.cldf_dir / 'contemporary',
                module='Generic',
                writer_cls=cldfbench.CLDFWriter,
            ),
        }

    def cmd_makecldf(self, args):
        gc_by_extension = collections.defaultdict(set)
        book, unattested, unclassifiable = set(), set(), set()
        for lg in args.glottolog.api.languoids():
            gc_by_extension[lg.id].add(lg.id)
            for _, gc, _ in lg.lineage:
                gc_by_extension[gc].add(lg.id)
                if gc == 'unat1236':
                    unattested.add(lg.id)
                if gc == 'book1242':
                    book.add(lg.id)
                if gc == 'uncl1493':
                    unclassifiable.add(lg.id)
        gc_by_extension = sorted(gc_by_extension.items(), key=lambda x: len(x[1]))

        # How to treat polygons assigned to multiple languages?
        # Status quo: Polygons are duplicated - thus, to figure out that multiple languages are
        # assigned to the same polygon, one would need to use shapely, e.g. computing overlap and
        # math.is_close or areas. It seems more correct, to just have one polygon and reference
        # that from multiple languages. In aggregations, this polygon would only show up if all
        # languoids are dialects of the same language or members of the same family.
        features = []

        def size(shp):
            mult = 100000000
            return int(shp.area * mult)

        areas = collections.defaultdict(list)
        for pid, f, gc in self.features:  # Group features by area.
            areas[size(f.shape)].append((pid, f, gc))
        for a, polys in sorted(areas.items(), key=lambda x: x[0]):
            if len(polys) > 1:
                gc = None
                # Only keep languages matched to non-bookkeeping Glottolog languoids.
                gcs = set(p[2] for p in polys if p[2] and p[2] not in book and p[2] not in unattested and p[2] not in unclassifiable)
                if len(gcs) > 1:
                    for gc, ext in gc_by_extension:
                        if ext.issuperset(gcs):
                            break  # All languoids are within one group. Match to this code, keep all names.
                    else:
                        pass  # Don't map to a Glottocode, keep all names.
                    # Reduce to one polygon, matched to the smallest Glottolog group
                    # containing all matched languoids.
                else:  # Use just one polygon, matched to the single Glottocode (but keep all names!)
                    gc = gcs.pop() if gcs else None

                assert int(size(intersection_all([p.shape for _, p, _ in polys]))) == a
                # Yield just one shape, with updated metadata.
                features.append((
                    list(sorted([pid for pid, _, _ in polys], key=lambda x: int(x.replace('x', '')))),
                    polys[0][1],
                    gc))
            else:  # All good, only one language mapped to the polygon.
                features.append(([polys[0][0]], polys[0][1], polys[0][2]))

        fi = self.feature_inventory
        for fid, v in fi.items():
            maps = [s.strip() for s in v.properties['map_name_full'].split('|') if s.strip()]
            numbers = [s.strip() for s in v.properties['number_legend'].split('|') if s.strip()]
            assert len(maps) == len(numbers), v.id
            v.properties['maps'] = ['{} [{}]'.format(m, n) for m, n in zip(maps, numbers)]

        def merge_properties(f, pids):
            # name, map_name_full, cldf:languageReference - remove number_legend
            f['properties']['name'] = ' | '.join(fi[pid].name for pid in pids)
            f['properties']['cldf:languageReference'] = '|'.join(fi[pid].glottocode for pid in pids if fi[pid].glottocode)
            f['properties']['maps'] = sorted(set(itertools.chain.from_iterable(fi[pid].properties['maps'] for pid in pids)))
            return f

        def is_(year, period):
            what = 'time of contact' if period == 'traditional' else period
            return year == what or year == '2007'

        for period in ['traditional', 'contemporary']:
            with (self.cldf_writer(args, cldf_spec=period) as writer):
                self.schema(writer.cldf)
                writer.cldf.properties['dc:title'] = \
                    ("{} speaker areas derived from Asher & Moseley 2007 "
                     "\"Atlas of the World's Languages\"").format(period.capitalize())
                #
                # FIXME: Add dc:description!
                #
                writer.cldf.add_columns(
                    'LanguageTable',
                    {'name': 'Maps', 'separator': '; '},
                )
                writer.cldf.add_columns(
                    'ContributionTable',
                    {'name': 'Maps', 'separator': '; '},
                    {'name': 'Equivalent_Feature_IDs', 'separator': ' '},
                )
                writer.cldf.add_sources(*Sources.from_file(self.etc_dir / "sources.bib"))

                fs = []
                for pids, f, gc in features:
                    years = {fi[pid].year for pid in pids}
                    assert len(years) == 1
                    if not is_(years.pop(), period):
                        continue
                    fs.append(merge_properties(f, pids))
                    writer.objects['ContributionTable'].append(dict(
                        ID=pids[0],
                        Name=f.properties['name'],
                        Glottocode=gc or None,
                        Source=[self.id],
                        Media_ID='features',
                        Maps=f.properties['maps'],
                        Equivalent_Feature_IDs=pids[1:],
                        Year='traditional' if fi[pids[0]].year == 'time of contact' else '2007',
                    ))
                dump(
                    feature_collection(
                        fs,
                        **{
                            'description': self.metadata.description,
                            'dc:isPartOf': self.metadata.title,
                        }),
                    writer.cldf_spec.dir / 'features.geojson')
                writer.objects['MediaTable'].append(dict(
                    ID='features',
                    Name='{} areas depicted in the source'.format(period),
                    Media_Type=MEDIA_TYPE,
                    Download_URL='features.geojson',
                ))

                shapes = [
                    (pids[0], f, gc) for pids, f, gc in features
                    if gc and is_(fi[pids[0]].year, period)]

                lids = None
                contribs = {c['ID']: c for c in writer.objects['ContributionTable']}
                for ptype in ['language', 'family']:
                    label = 'languages' if ptype == 'language' else 'families'
                    p = writer.cldf_spec.dir / '{}.geojson'.format(label)
                    ffs, languages = aggregate(
                        shapes,
                        args.glottolog.api,
                        level=ptype,
                        buffer=0.005,
                        opacity=0.5)
                    dump(
                        feature_collection(
                            ffs,
                            title='Speaker areas for {} ({})'.format(label, period),
                            description='Speaker areas aggregated for Glottolog {}-level languoids, '
                            'color-coded by family.'.format(ptype)),
                    p)
                    for (glang, pids, family), f in zip(languages, ffs):
                        if lids is None or (glang.id not in lids):  # Don't append isolates twice!
                            writer.objects['LanguageTable'].append(dict(
                                ID=glang.id,
                                Name=glang.name,
                                Glottocode=glang.id,
                                Latitude=glang.latitude,
                                Longitude=glang.longitude,
                                Feature_IDs=pids,
                                Maps=sorted(set(itertools.chain.from_iterable(contribs[pid]['Maps'] for pid in pids))),
                                Speaker_Area=p.stem,
                                Glottolog_Languoid_Level=ptype,
                                Family=family,
                            ))
                    writer.objects['MediaTable'].append(dict(
                        ID=p.stem,
                        Name='Speaker areas for {} ({})'.format(label, period),
                        Description='Speaker areas aggregated for Glottolog {}-level languoids, '
                                    'color-coded by family.'.format(ptype),
                        Media_Type=MEDIA_TYPE,
                        Download_URL=p.name,
                    ))
                    lids = {gl.id for gl, _, _ in languages}

            writer.cldf.properties['dc:spatial'] = \
                ('westlimit={:.1f}; southlimit={:.1f}; eastlimit={:.1f}; northlimit={:.1f}'.format(
                    *self.bounds))

    def cmd_readme(self, args):
        minlon, minlat, maxlon, maxlat = self.bounds
        coords = [[
            (minlon, minlat),
            (minlon, maxlat),
            (maxlon, maxlat),
            (maxlon, minlat),
            (minlon, minlat)
        ]]
        f = json.dumps(Feature.from_geometry(dict(type='Polygon', coordinates=coords)))
        return add_markdown_text(
            cldfbench.Dataset.cmd_readme(self, args),
            """
This Glottography dataset provides **two** sets of speaker areas for the languages of the world:
- *contemporary* speaker areas ([cldf/contemporary](cldf/contemporary/)) and
- *traditional* (aka "time of contact") speaker areas ([cldf/traditional](cldf/traditional/));

following the distinction made by Asher &amp; Moseley 2007 for their maps of the Americas and Australia.
In order to provide two sets with global coverage, we supplemented the *traditional* set with the
areas depicted in the contemporary maps for the other macroareas, taking current distribution as proxy
for time-of-contact data in regions presumably less affected by colonialism.


### Coverage

```geojson
{}
```
""".format(f),
            'Description')
