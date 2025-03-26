# Releasing the dataset

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_asher2007world.py
```

```shell
cldfbench makecldf cldfbench_asher2007world.py --glottolog-version v5.1
```

This create **two** CLDF datasets, one with *traditional* speaker areas, and one with *contemporary*
areas.


## Validation


### The *traditional* areas

Run CLDF validation and validation of geometries:
```shell
cldf validate cldf/traditional
cldfbench geojson.validate cldf/traditional
```

#### Glottolog distance

Compute distances of language-level speaker areas to corresponding Glottolog point coordinate:
```shell
cldfbench geojson.glottolog_distance cldf/traditional --format tsv | csvformat -t > etc/traditional/glottolog_distance.csv
```

Print the unexplained cases with distance >= 1 grid unit:
```shell
csvjoin --left -c ID etc/traditional/glottolog_distance.csv etc/glottolog_distance_known.csv | csvgrep -c Distance -r"^0\.?" -i | csvgrep -i -c note -r".+" | csvsort -c Distance | csvcut -c ID,Distance | csvformat -E | termgraph
```
FIXME: maake sure no distances > 2.


```shell
csvjoin --left -c ID etc/traditional/glottolog_distance.csv etc/glottolog_distance_known.csv | csvgrep -c Distance -r"^0\.?" -i | csvgrep -i -c note -r".+" | csvsort -c Distance | csvcut -c ID | cldfbench geojson.geojson --glottolog-version v5.1 cldf/traditional -  > etc/traditional/glottolog_distance_outliers.geojson
```

#### MultiPolygon spread

```shell
cldfbench geojson.multipolygon_spread cldf/traditional --format tsv | csvformat -t > etc/traditional/multipolygon_spread.csv
```

```shell
csvjoin --left -c ID etc/traditional/multipolygon_spread.csv etc/multipolygon_spread_known.csv | csvgrep -c Spread -r"^0\.?" -i | csvgrep -i -c note -r".+" | csvsort -c Spread | csvcut -c ID,Spread | csvformat -E | termgraph
```
There should be no unexplained spread > 4.

Investigate multi-polygons with spread >= 3:
```shell
csvjoin --left -c ID etc/traditional/multipolygon_spread.csv etc/multipolygon_spread_known.csv | csvgrep -c Spread -r"^([012])\.?" -i | csvgrep -i -c note -r".+" | csvsort -c Spread | csvcut -c ID | cldfbench geojson.geojson --glottolog-version v5.1 cldf/traditional -  > etc/traditional/multipolygon_spread_outliers.geojson
```

Investigate multi-polygons with spread >=1, consisting of only 2 polygons:
```shell
csvjoin --left -c ID etc/traditional/multipolygon_spread.csv etc/multipolygon_spread_known.csv | csvgrep -c Spread -r"^0\.?" -i | csvgrep -i -c note -r".+" | csvgrep -c NPolys -r"^([12])$" | csvsort -c Spread | csvcut -c ID | cldfbench geojson.geojson --glottolog-version v5.1 cldf/traditional -  > etc/traditional/multipolygon_spread_outliers.geojson
```



### The *contemporary* areas

Run CLDF validation and validation of geometries:
```shell
cldf validate cldf/contemporary
cldfbench geojson.validate cldf/contemporary
```

#### Glottolog distance

Compute distances of language-level speaker areas to corresponding Glottolog point coordinate:
```shell
cldfbench geojson.glottolog_distance cldf/contemporary --format tsv | csvformat -t > etc/contemporary/glottolog_distance.csv
```

Print the unexplained cases with distance >= 1 grid unit:
```shell
csvjoin --left -c ID etc/contemporary/glottolog_distance.csv etc/glottolog_distance_known.csv | csvgrep -c Distance -r"^0\.?" -i | csvgrep -i -c note -r".+" | csvsort -c Distance | csvcut -c ID,Distance | csvformat -E | termgraph
```
FIXME: make sure no distances > 10.

Distances can generally be explained by displacement of populations during colonialism.
```shell
csvjoin --left -c ID etc/contemporary/glottolog_distance.csv etc/glottolog_distance_known.csv | csvgrep -c Distance -r"^(0|1)\.?" -i | csvgrep -i -c note -r".+" | csvsort -c Distance | csvcut -c ID | cldfbench geojson.geojson --glottolog-version v5.1 cldf/contemporary -  > etc/contemporary/glottolog_distance_outliers.geojson
```


#### MultiPolygon spread

```shell
cldfbench geojson.multipolygon_spread cldf/contemporary --format tsv | csvformat -t > etc/contemporary/multipolygon_spread.csv
```

```shell
csvjoin --left -c ID etc/contemporary/multipolygon_spread.csv etc/multipolygon_spread_known.csv | csvgrep -c Spread -r"^0\.?" -i | csvgrep -i -c note -r".+" | csvsort -c Spread | csvcut -c ID,Spread | csvformat -E | termgraph
```
There should be no unexplained spread > 4.

Investigate multi-polygons with spread >= 3:
```shell
csvjoin --left -c ID etc/contemporary/multipolygon_spread.csv etc/multipolygon_spread_known.csv | csvgrep -c Spread -r"^([012])\.?" -i | csvgrep -i -c note -r".+" | csvsort -c Spread | csvcut -c ID | cldfbench geojson.geojson --glottolog-version v5.1 cldf/contemporary -  > etc/contemporary/multipolygon_spread_outliers.geojson
```
These generally "make sense".

Investigate multi-polygons with spread >=1, consisting of only 2 polygons:
```shell
csvjoin --left -c ID etc/contemporary/multipolygon_spread.csv etc/multipolygon_spread_known.csv | csvgrep -c Spread -r"^0\.?" -i | csvgrep -i -c note -r".+" | csvgrep -c NPolys -r"^([12])$" | csvsort -c Spread | csvcut -c ID | cldfbench geojson.geojson --glottolog-version v5.1 cldf/contemporary -  > etc/contemporary/multipolygon_spread_outliers.geojson
```
They also look reasonable.




## Creating metadata


```shell
cldfbench cldfreadme cldfbench_asher2007world.py
```

```shell
cldfbench zenodo cldfbench_asher2007world.py
```

```shell
cldfbench readme cldfbench_asher2007world.py
```
