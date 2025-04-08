# CLDF datasets

- [Generic: Traditional speaker areas derived from Asher & Moseley 2007 "Atlas of the World's Languages"](#ds-traditionalmetadatajson)
- [Generic: Contemporary speaker areas derived from Asher & Moseley 2007 "Atlas of the World's Languages"](#ds-contemporarymetadatajson)

<a name="ds-traditionalmetadatajson"> </a>

# Generic Traditional speaker areas derived from Asher & Moseley 2007 "Atlas of the World's Languages"

**CLDF Metadata**: [traditional-metadata.json](traditional/traditional-metadata.json)

**Sources**: [sources.bib](traditional/sources.bib)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Asher, R. E. & Christopher J. Moseley (eds.) 2007. Atlas of the World's Languages. 2nd edn. Routledge.
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Generic](http://cldf.clld.org/v1.0/terms.rdf#Generic)
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/Glottography/asher2007world
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/Glottography/asher2007world/tree/7555d4a">Glottography/asher2007world status-quo-ante-33-g7555d4a</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v5.1">Glottolog v5.1</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.12.3</li><li><strong>python-packages</strong>: <a href="traditional/requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | asher2007world
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-mediacsv"></a>Table [media.csv](traditional/media.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF MediaTable](http://cldf.clld.org/v1.0/terms.rdf#MediaTable)
[dc:extent](http://purl.org/dc/terms/extent) | 3


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Media_Type](http://cldf.clld.org/v1.0/terms.rdf#mediaType) | `string`<br>Regex: `[^/]+/.+` | 
[Download_URL](http://cldf.clld.org/v1.0/terms.rdf#downloadUrl) | `anyURI` | 
[Path_In_Zip](http://cldf.clld.org/v1.0/terms.rdf#pathInZip) | `string` | 

## <a name="table-languagescsv"></a>Table [languages.csv](traditional/languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 4610


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal`<br>&ge; -90<br>&le; 90 | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal`<br>&ge; -180<br>&le; 180 | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string`<br>Regex: `[a-z0-9]{4}[1-9][0-9]{3}` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string`<br>Regex: `[a-z]{3}` | 
[Feature_IDs](http://cldf.clld.org/v1.0/terms.rdf#contributionReference) | list of `string` (separated by ` `) | List of identifiers of features that were aggregated to create the feature referenced by Speaker_Area.<br>References [contributions.csv::ID](#table-contributionscsv)
`Glottolog_Languoid_Level` | `string`<br>Valid choices:<br> `dialect` `language` `family` | https://glottolog.org/meta/glossary#Languoid
`Family` | `string` | Name of the top-level family for the languoid in the Glottolog classification. A null value in this column marks 1) top-level families in case Glottolog_Languoid_Level is 'family' and 2) isolates in case Glottolog_Languoid_Level is 'language'.
[Speaker_Area](http://cldf.clld.org/v1.0/terms.rdf#speakerArea) | `string` | References [media.csv::ID](#table-mediacsv)
`Maps` | list of `string` (separated by `; `) | 

## <a name="table-contributionscsv"></a>Table [contributions.csv](traditional/contributions.csv)

We list the individual features from the source dataset as contributions in order to preserve the original metadata and a point of reference for the aggregated shapes.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ContributionTable](http://cldf.clld.org/v1.0/terms.rdf#ContributionTable)
[dc:extent](http://purl.org/dc/terms/extent) | 6095


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Contributor](http://cldf.clld.org/v1.0/terms.rdf#contributor) | `string` | 
[Citation](http://cldf.clld.org/v1.0/terms.rdf#citation) | `string` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string`<br>Regex: `[a-z0-9]{4}[1-9][0-9]{3}` | References a Glottolog languoid most closely matching the linguistic entity described by the feature.
[Year](http://purl.org/dc/terms/temporal) | `string`<br>Regex: `[0-9]{3,4}|traditional` | The time period to which the feature relates, specified as year AD or with the keyword 'traditional', meaning either the time of contact with European maritime powers or period when an ancient language was spoken.
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](traditional/sources.bib)
[Media_ID](http://cldf.clld.org/v1.0/terms.rdf#mediaReference) | `string` | Features are linked to GeoJSON files that store the geo data.<br>References [media.csv::ID](#table-mediacsv)
`Map_Name` | `string` | Name of the map as given in the source publication.
`Maps` | list of `string` (separated by `; `) | 
`Equivalent_Feature_IDs` | list of `string` (separated by ` `) | 


<a name="ds-contemporarymetadatajson"> </a>

# Generic Contemporary speaker areas derived from Asher & Moseley 2007 "Atlas of the World's Languages"

**CLDF Metadata**: [contemporary-metadata.json](contemporary/contemporary-metadata.json)

**Sources**: [sources.bib](contemporary/sources.bib)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Asher, R. E. & Christopher J. Moseley (eds.) 2007. Atlas of the World's Languages. 2nd edn. Routledge.
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Generic](http://cldf.clld.org/v1.0/terms.rdf#Generic)
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/Glottography/asher2007world
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/Glottography/asher2007world/tree/7555d4a">Glottography/asher2007world status-quo-ante-33-g7555d4a</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v5.1">Glottolog v5.1</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.12.3</li><li><strong>python-packages</strong>: <a href="contemporary/requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | asher2007world
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-mediacsv"></a>Table [media.csv](contemporary/media.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF MediaTable](http://cldf.clld.org/v1.0/terms.rdf#MediaTable)
[dc:extent](http://purl.org/dc/terms/extent) | 3


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Media_Type](http://cldf.clld.org/v1.0/terms.rdf#mediaType) | `string`<br>Regex: `[^/]+/.+` | 
[Download_URL](http://cldf.clld.org/v1.0/terms.rdf#downloadUrl) | `anyURI` | 
[Path_In_Zip](http://cldf.clld.org/v1.0/terms.rdf#pathInZip) | `string` | 

## <a name="table-languagescsv"></a>Table [languages.csv](contemporary/languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 4189


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal`<br>&ge; -90<br>&le; 90 | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal`<br>&ge; -180<br>&le; 180 | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string`<br>Regex: `[a-z0-9]{4}[1-9][0-9]{3}` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string`<br>Regex: `[a-z]{3}` | 
[Feature_IDs](http://cldf.clld.org/v1.0/terms.rdf#contributionReference) | list of `string` (separated by ` `) | List of identifiers of features that were aggregated to create the feature referenced by Speaker_Area.<br>References [contributions.csv::ID](#table-contributionscsv)
`Glottolog_Languoid_Level` | `string`<br>Valid choices:<br> `dialect` `language` `family` | https://glottolog.org/meta/glossary#Languoid
`Family` | `string` | Name of the top-level family for the languoid in the Glottolog classification. A null value in this column marks 1) top-level families in case Glottolog_Languoid_Level is 'family' and 2) isolates in case Glottolog_Languoid_Level is 'language'.
[Speaker_Area](http://cldf.clld.org/v1.0/terms.rdf#speakerArea) | `string` | References [media.csv::ID](#table-mediacsv)
`Maps` | list of `string` (separated by `; `) | 

## <a name="table-contributionscsv"></a>Table [contributions.csv](contemporary/contributions.csv)

We list the individual features from the source dataset as contributions in order to preserve the original metadata and a point of reference for the aggregated shapes.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ContributionTable](http://cldf.clld.org/v1.0/terms.rdf#ContributionTable)
[dc:extent](http://purl.org/dc/terms/extent) | 5573


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Contributor](http://cldf.clld.org/v1.0/terms.rdf#contributor) | `string` | 
[Citation](http://cldf.clld.org/v1.0/terms.rdf#citation) | `string` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string`<br>Regex: `[a-z0-9]{4}[1-9][0-9]{3}` | References a Glottolog languoid most closely matching the linguistic entity described by the feature.
[Year](http://purl.org/dc/terms/temporal) | `string`<br>Regex: `[0-9]{3,4}|traditional` | The time period to which the feature relates, specified as year AD or with the keyword 'traditional', meaning either the time of contact with European maritime powers or period when an ancient language was spoken.
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](contemporary/sources.bib)
[Media_ID](http://cldf.clld.org/v1.0/terms.rdf#mediaReference) | `string` | Features are linked to GeoJSON files that store the geo data.<br>References [media.csv::ID](#table-mediacsv)
`Map_Name` | `string` | Name of the map as given in the source publication.
`Maps` | list of `string` (separated by `; `) | 
`Equivalent_Feature_IDs` | list of `string` (separated by ` `) | 

