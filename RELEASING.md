# Releasing the dataset

Recreate the CLDF datasets:
```shell
cldfbench makecldf cldfbench_asher2007world.py --glottolog-version v5.2
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
