#!/usr/bin/env python3

import sys

def load_city_data(path):
    """Load city longitude ranges from CSV file at the provided path.
    Return a sorted list of tuples where each tuple is (lng_min, lng_max, city)."""
    data = []
    with open(path, 'r') as f:
        next(f) # skip header
        for line in f:
            city, lng_min, lng_max = line.split(',')
            lng_min, lng_max = float(lng_min), float(lng_max)
            data.append((lng_min, lng_max, city))
    return sorted(data)

def find_intersections(city_data, longitudes):
    """Look up each input longitude against `city_data` and print the number of
    cities intersected by the longitude. Output is CSV: `lng,num_cities`."""
    print('lng,num_cities')
    for line in longitudes:
        intersected = set()
        lng = float(line)
        for lng_min, lng_max, city in city_data:
            if lng >= lng_min and lng <= lng_max:
                intersected.add(city)
        print('{},{}'.format(lng, len(intersected)))

args = sys.argv[1:]
if len(args) < 1:
    print('\nUSAGE: ./longitude.py CITIES_PATH')
    print('\nProvide input longitudes via STDIN.')
    sys.exit(1)

city_data = load_city_data(args.pop(0))
find_intersections(city_data, sys.stdin)
