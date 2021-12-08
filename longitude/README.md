# Overview

The script `longitude.py` takes in longitude lines as input, and prints the number of cities
intersected by each input longitude line. The program uses a database (loaded from CSV) containing
the longitude ranges covered by cities around the world.

## Problem

Your task is to process 4 million input longitudes.

The current implementation of `longitude.py` is very inefficient. Out of the box, it likely won't
finish before the end of the exercise. Feel free to use anything in your toolset to complete the
task, and please ask questions to clarify requirements as needed.

# Instructions

1. Run `./random_longitude.py cities.csv 4000000 > input.csv`.
2. Run `cat input.csv | ./longitude.py cities.csv`.

# Details

## Example

Suppose `cities.csv` contains just two cities:

    city,lng_min,lng_max
    Mumbai,72.8,73.0
    Atlanta,-84.42,-84.27

Then, given the input longitude `72.9`, the script would report that exactly one city is
intersected by `72.9` (Mumbai):

    $ echo '72.9' | ./longitude.py cities.csv
    lng,num_cities
    72.9,1

## Files

    .
    ├── longitude.py          # main program
    ├── cities.csv            # cities database
    └── random_longitude.py   # input generator
