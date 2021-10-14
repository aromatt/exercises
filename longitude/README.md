# Overview

The script `longitude.py` takes in lines of longitude as input, and outputs the number of cities
intersected by each input longitude line. The program uses a database (loaded from CSV) containing
city longitude ranges.

## Problem

Your task is to process 1 million input longitudes.

The current implementation of `longitude.py` is very inefficient. Out of the box, it likely won't
finish before the end of the exercise. Feel free to use anything in your toolset to complete the
task, and please ask questions to clarify requirements as needed.

# Instructions

1. Run `./gen_input.py cities.csv 1000000 > input.csv`.
2. Run `./longitude.py cities.csv input.csv`.

Note: you can also provide input via STDIN: `cat input.csv | ./longitude.py cities.csv`.

# Details

## Example

Suppose `cities.csv` contains just two cities:

    city,lng_min,lng_max
    Mumbai,72.8,73.0
    Atlanta,-84.42,-84.27

Then, given the input longitude `72.9`, the script would report that exactly one city is
intersected (Mumbai).

## Files

    .
    ├── longitude.py   # main program
    ├── cities.csv     # cities database
    └── gen_input.py   # input generator

## Formats

### `cities.csv`

    city,lng_min,lng_max
    Atlanta,-84.42,-84.27
    ...

### `input.csv`

    161.8
    -102.71
    ...

### Output of `longitude.py`:

    lng,num_cities
    161.8,0
    -102.71,11
    ...
