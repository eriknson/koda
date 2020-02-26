#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from google.transit import gtfs_realtime_pb2
import gzip
import os
import datetime

directory = './data/30/'
feedEntitiesPerDay={}

# Loop through all files in directory
for filename in os.listdir(directory):
    if (filename != '.DS_Store'):
        print(filename + ' read')
        
        # Uncompress and parse protobuff-file using gtfs_realtime_pb2
        with gzip.open('./data/30/' + filename, 'rb') as file:
            response = file.read()
            feed = gtfs_realtime_pb2.FeedMessage()
            feed.ParseFromString(response)
            
            # Create entry (key) for each day with lists of all feed entities as values
            for entity in feed.entity:
                feedEntitiesPerDay.setdefault(entity.trip_update.trip.start_date,[]).append(entity)

trips = {}

# Loop throgh all FeedEntities in a specific day and create dictionary with unique trip id's and corresponding entity timestamps
for entity in feedEntitiesPerDay['20200130']:
    trips.setdefault(entity.trip_update.trip.trip_id,[]).append(datetime.datetime.fromtimestamp(entity.trip_update.timestamp).strftime('%H:%M:%S'))
    
    
entities = {}

for entity in feedEntitiesPerDay['20200130']:
    entities.setdefault(entity.id,[]).append(entity.trip_update)
    
for entry in entities:
    print(entities[entry])