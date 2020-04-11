#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:03:37 2020

@author: x
"""

from google.transit import gtfs_realtime_pb2
import sched, time
import requests

s = sched.scheduler(time.time, time.sleep)

vehicleDict = {}

def requestVehiclePositions(sc): 
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://opendata.samtrafiken.se/ul/VehiclePositions.pb?key=8e90cd12622a49449e473869721ca908')
    feed.ParseFromString(response.content)
    
    vehicleDict[feed.header.timestamp]=[]
    
    for entity in feed.entity:
        print(entity)
        if entity.vehicle.trip.trip_id:       
            vehicleDict[feed.header.timestamp].append({
                                'vehicleID':entity.id,
                                'trip':entity.vehicle.trip.trip_id,
                                'lat':entity.vehicle.position.latitude,
                                'lon':entity.vehicle.position.longitude,
                                'speed':entity.vehicle.position.speed,
                                'bearing':entity.vehicle.position.bearing,
                                'timestamp':entity.vehicle.timestamp
                               })
        s.enter(3, 1, requestVehiclePositions, (sc,))

s.enter(3, 1, requestVehiclePositions, (s,))
s.run()

