# Releasing the dataset

Recreate the CLDF datasets:
```shell
cldfbench makecldf cldfbench_asher2007world.py --glottolog-version v5.2
```

This creates **two** CLDF datasets, one with *traditional* speaker areas, and one with *contemporary*
areas.

Validate the datasets by following the instructions at [VALIDATION.md](VALIDATION.md).


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


## Release

Run
```shell
cldfbench glottography.release cldfbench_asher2007world.py vX.Y
```
and follow the instructions given in the output of the command.
