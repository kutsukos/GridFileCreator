# GridFile Creator


### Usage
```console
$ python3 GridFileCreator.py
```

### Inputs
A file called data.dat
Input file format:   <chromosome_number> <starting_point> <ending_point> <number_of_points_in_between>

Input file format example:
```console
1 100 220 7
8 50 680 5 
```
This file is defining the data to be used by the script. We can have multiple lines to generate multiple files for the same or different chromosomes.


### ABOUT GridFile Creator 
This tool is creating **tab-delimited files**, that contains points inside a specified range.
The start and the end of the range is included on this file.

It can be used as input in some programs like SweeD or OmegaPlus.


### Example
if we use the data.dat file, included in this repo and we execute the script, we expect 2 files. One file for chromosome 1 and one file for chromosome 2.

```console
$ python3 GridFileCreator.py
Grid File Creator
Grid File Creator: Reading input file
Grid File Creator: Writing on output file/s
Grid File Creator: Creating points completed

$ cat points.1.100.220.5.out
chr1    100
chr1    120
chr1    140
chr1    160
chr1    180
chr1    200
chr1    220

cat points.2.100.220.7.out
chr2    100
chr2    115
chr2    130
chr2    145
chr2    160
chr2    175
chr2    190
chr2    205
chr2    220
```


## Contact
Contact me at ioannis.kutsukos@gmail.com for reporting bugs or anything else! :)
