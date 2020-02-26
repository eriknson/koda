#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from google.transit import gtfs_realtime_pb2
import gzip
import os

directory = './data/30/'
days={}

# Loop through all files in directory
for filename in os.listdir(directory):
    if (filename != '.DS_Store'):
        print(filename + ' read')
        
        # Uncompress and parse protobuff-file using gtfs_realtime_pb2
        with gzip.open('./data/30/' + filename, 'rb') as file:
            response = file.read()
            feed = gtfs_realtime_pb2.FeedMessage()
            feed.ParseFromString(response)
            
            # Create entry for each day (key) with all feed entities as values
            for entity in feed.entity:
                days.setdefault(entity.trip_update.trip.start_date,[]).append(entity)
                
#for trip in trips['20200128']:
#    print(time.localtime(trip.trip_update.timestamp).tm_hour,':',time.localtime(trip.trip_update.timestamp).tm_min,':',time.localtime(trip.trip_update.timestamp).tm_sec)
                

trips = {}

for entity in days['20200130']:
    trips.setdefault(entity.trip_update.trip.trip_id,[]).append(entity.trip_update.timestamp)