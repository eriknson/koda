#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API key: 270394d8f8c74e5191d4f235e8dd925e
"""

# -*- coding: utf-8 -*-

import csv

stopDict = {}

with open('./gtfs_static_data_ul/stops.csv') as file:
    reader = csv.DictReader(file)
    # Create dictionary entry for each row in stops.csv
    for row in reader:
        stopDict[row['stop_id']]={'stop_name':row['stop_name'],'stop_trip_id_list':[],'stop_lat':row['stop_lat'],'stop_lon':row['stop_lon']}

with open('./gtfs_static_data_ul/stop_times.csv') as file:
    reader = csv.DictReader(file)
    # Append each stops' matching trip id(s) from stop_times.csv
    for row in reader:
        stopDict[row['stop_id']].get('stop_trip_id_list').append(row['trip_id'])
        print(stopDict[row['stop_id']].get('stop_trip_id_list'))
        

