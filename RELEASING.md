# Releasing the dataset

In case of upstream changes in glottography-data we have to recreate the GeoJSON dataset in `raw/`
and`metadata.json`, running
```shell
cldfbench download cldfbench_asher2007world.py
```

Now we can recreate the CLDF datasets:
```shell
cldfbench makecldf cldfbench_asher2007world.py --glottolog-version v5.1
```

This creates **two** CLDF datasets, one with *traditional* speaker areas, and one with *contemporary*
areas.


## Creating metadata


```shell
cldfbench cldfreadme cldfbench_asher2007world.py
```

```shell
cldfbench zenodo cldfbench_asher2007world.py --communities="glottography,cldf-datasets"
```

```shell
cldfbench readme cldfbench_asher2007world.py
```
