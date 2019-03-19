# GridFile Creator
![dependencies](https://img.shields.io/badge/python-2.7-informational.svg)

## Usage
Usage: python createPointsInARangeDefinedinCLI.py -h



## ABOUT GridFile Creator 

This tool is creating a tab-delimited file, that contains positions inside a specified range.

It can be used as input in some programs like SweeD or OmegaPlus.

The format of this file is "chr <tab> pos". The following example, will make it clear!

It is like a bed file, but it is not defining areas of interest, but points, inside an area.



## EXAMPLE
-----------------------------
```bash
$ python GridFileCreator.py -c 1 -s 100 -e 220 -n 7

[Creating points completed]
Area: 100 - 220
Distance:20
[DEBUGGING MSG] 7/7 points created and exported to points.1.100.220.out


$ cat points.1.100.220.out

chr1	100
chr1	120
chr1	140
chr1	160
chr1	180
chr1	200
chr1	220
```



## VERSION CHANGELOG
##### -0.1
+dist argument inserted

+help

##### -0.2 - CURRENT
+bugs with arguments solved

## Contact
Contact me at skarisg@gmail.com for reporting bugs or anything else! :)
