#!/usr/bin/env python3

import random
import sys
import os

def generate(city_data, count):
    random.seed(os.environ.get('SEED', '0'))
    print('Generating {} rows of input data'.format(count), file=sys.stderr)
    for i in range(count):
        if i % (count / 10) == 0:
            print(i, file=sys.stderr)
        if random.random() > 0.33:
            lng_min, lng_max, _ = random.choice(city_data)
            lng = round(random.uniform(lng_min, lng_max), 2)
        else:
            lng = round(random.uniform(0, 180), 2)
        print(str(lng))

def load_city_data(path):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        next(f) # skip header
        for line in f:
            city, lng_min, lng_max = line.split(',')
            lng_min, lng_max = float(lng_min), float(lng_max)
            data.append((lng_min, lng_max, city))
    return sorted(data)

if len(sys.argv) != 3:
    print('USAGE: ./random_longitude.py CITY_DATA COUNT')
    sys.exit(1)

city_data_path = sys.argv[1]
count = int(sys.argv[2])
city_data = load_city_data(city_data_path)
generate(city_data, count)
