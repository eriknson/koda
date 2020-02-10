# -*- coding: utf-8 -*-

import requests
import json

# Get all stop points

#response = requests.get('http://api.sl.se/api2/LineData.json?model=stoppoint&key=461aca8d48264b3f9a3f31d701fce8f8')
#listOfStops = response.json()
#result = listOfStops.get('ResponseData').get('Result')
#for stop in result:
#    print(stop.get('StopPointName'))
    
response1 = requests.get('http://api.sl.se/api2/LineData.json?model=stoppoint&key=461aca8d48264b3f9a3f31d701fce8f8')
response2 = requests.get('http://api.sl.se/api2/LineData.json?model=JourneyPatternPointOnLine&key=461aca8d48264b3f9a3f31d701fce8f8')
locationOfStops = response1.json()
listOfStops = response2.json()

result1 = locationOfStops.get('ResponseData').get('Result')
result2 = listOfStops.get('ResponseData').get('Result')

graphData = {}

for stop in result1:
    graphData.update({stop.get('StopPointNumber') : {'lon':stop.get('LocationEastingCoordinate'),'lat':stop.get('LocationNorthingCoordinate')}})

for stop in result2:
    graphData.update({stop.get('JourneyPatternPointNumber') : {'line':[stop.get('LineNumber')]}})
