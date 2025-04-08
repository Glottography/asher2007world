# Glottography dataset derived from Asher and Moseley 2007 "Atlas of the World's Languages"

[![CLDF validation](https://github.com/Glottography/asher2007world/workflows/CLDF-validation/badge.svg)](https://github.com/Glottography/asher2007world/actions?query=workflow%3ACLDF-validation)

## How to cite

If you use these data please cite
- the original source
  > Asher, R. E. & Christopher J. Moseley (eds.) 2007. Atlas of the World's Languages. 2nd edn. Routledge.
- the derived dataset using the DOI of the [particular released version](../../releases/) you were using

## Description


This dataset is licensed under a CC-BY-4.0 license



This Glottography dataset provides **two** sets of speaker areas for the languages of the world:
- *contemporary* speaker areas ([cldf/contemporary](cldf/contemporary/)) and
- *traditional* (aka "time of contact") speaker areas ([cldf/traditional](cldf/traditional/));

following the distinction made by Asher &amp; Moseley 2007 for their maps of the Americas and Australia.
In order to provide two sets with global coverage, we supplemented the *traditional* set with the
areas depicted in the contemporary maps for the other macroareas, taking current distribution as proxy
for time-of-contact data in regions presumably less affected by colonialism.


### Coverage

```geojson
{"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[-171.9, -56.0], [-171.9, 80.6], [180.0, 80.6], [180.0, -56.0], [-171.9, -56.0]]]}, "properties": {}}
```


## CLDF Datasets

The following CLDF datasets are available in [cldf](cldf):

- CLDF [Generic](https://github.com/cldf/cldf/tree/master/modules/Generic) at [cldf/traditional/traditional-metadata.json](cldf/traditional/traditional-metadata.json)
- CLDF [Generic](https://github.com/cldf/cldf/tree/master/modules/Generic) at [cldf/contemporary/contemporary-metadata.json](cldf/contemporary/contemporary-metadata.json)