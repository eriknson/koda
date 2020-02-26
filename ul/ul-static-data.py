#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API key: 270394d8f8c74e5191d4f235e8dd925e
"""

# -*- coding: utf-8 -*-

import csv

stops = {}
stopsOnTrip = {}
routeStations = {}
routeTrips = {}
tripRoute = {}
routeShortNames = {}

with open('./gtfs_static_data_ul/stops.csv') as file:
    reader = csv.DictReader(file)
    # Create dictionary key for each row in stops.csv with values on name, latitude and longitude
    for row in reader:
        stops[row['stop_id']] = {'stop_name': row['stop_name'],
                                 'stop_lat': row['stop_lat'], 'stop_lon': row['stop_lon']}


with open('./gtfs_static_data_ul/stop_times.csv') as file:
    reader1 = csv.DictReader(file)
    # Loops through stop_times.csv and creates dictionary with stops per unique trip
    for row in reader1:
        if row['trip_id'] not in stopsOnTrip:
            stopsOnTrip[row['trip_id']] = [stops[row['stop_id']]]
        if row['trip_id'] in stopsOnTrip:
            stopsOnTrip[row['trip_id']].append(stops[row['stop_id']])


with open('./gtfs_static_data_ul/trips.csv') as file:
    reader2 = csv.DictReader(file)
    # Loops through trips.csv and creates dictionary with the first trip per unique route
    for row in reader2:
        if row['route_id'] not in routeStations:
            routeStations[row['route_id']] = stopsOnTrip[row['trip_id']]
       
        
with open('./gtfs_static_data_ul/trips.csv') as file:
    reader3 = csv.DictReader(file)
    # Creates a dictionary with all unique trip_id:s per unique route_id
    for row in reader3:
        routeTrips.setdefault((row['direction_id'],row['route_id']),[]).append(row['trip_id'])
        
with open('./gtfs_static_data_ul/routes.csv') as file:
    reader4 = csv.DictReader(file)
    # Creates a dictionary with all unique route_id:s and corresponding route_short_name
    for row in reader4:
        routeShortNames.setdefault(row['route_id'],[]).append(row['route_short_name'])
        
with open('./gtfs_static_data_ul/trips.csv') as file:
    reader5 = csv.DictReader(file)
    # Creates a dictionary with all unique trip_id:s per unique route_id
    for row in reader5:
        tripRoute[row['trip_id']] = { 'route':row['route_id'],'direction':row['direction_id'] }