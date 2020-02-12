#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:36:41 2020

@author: axelboman
"""
"playing with UL static data"

import csv 
import pandas as pd


stopData = pd.read_csv('gtfs_static_data_ul/stops.csv')
tripData = pd.read_csv('gtfs_static_data_ul/trips.csv')
routeData = pd.read_csv('gtfs_static_data_ul/routes.csv')
stopTimeData = pd.read_csv('gtfs_static_data_ul/stop_times.csv')
shapesData = pd.read_csv('gtfs_static_data_ul/shapes.csv')


routeDict = {}
tripDict = {}
finalDict ={}

#extract columns route_id and trip_id from tripData 
route_ids = tripData[['route_id','trip_id']]

#iterate over all rows and append all trip_id to tripList and create dictornary with all 
#routes as key and 1 of the corresponding trips on that route
for index, row in route_ids.iterrows():
    routeDict[row['route_id']] = row['trip_id']
    print(routeDict)
    
    
#extract columns trip_id and stop_id from stopTimeData 
trip_ids = stopTimeData[['trip_id','stop_id']]

#iterate over all rows and create dictornary with all 
#trips as key and the stop_ids for each trip
for index, row in trip_ids.iterrows():
    tripDict[row['trip_id']] = row['stop_id']
    
for trip in tripDict:
    
    for route in routeDict:
        
        
    
    

        
      
    
    
    


