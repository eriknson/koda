# -*- coding: utf-8 -*-

import requests
import json

# Get all stop points

#response = requests.get('http://api.sl.se/api2/LineData.json?model=stoppoint&key=461aca8d48264b3f9a3f31d701fce8f8')
#listOfStops = response.json()
#result = listOfStops.get('ResponseData').get('Result')
#for stop in result:
#    print(stop.get('StopPointName'))
    
api_response1 = requests.get('http://api.sl.se/api2/LineData.json?model=stoppoint&key=461aca8d48264b3f9a3f31d701fce8f8')
api_response2 = requests.get('http://api.sl.se/api2/LineData.json?model=JourneyPatternPointOnLine&key=461aca8d48264b3f9a3f31d701fce8f8')

locationOfStops = api_response1.json().get('ResponseData').get('Result')
stopsAndLines = api_response2.json().get('ResponseData').get('Result')

stopDict = {"1337":{"lon":1,"lat":2}}

for stop in locationOfStops:
    stopDict[stop.get('StopPointNumber')] = {'lon':stop.get('LocationEastingCoordinate'),'lat':stop.get('LocationNorthingCoordinate'),'line':[]}
    
for stop in stopsAndLines:
    stopID=stop.get('JourneyPatternPointNumber')
    stopLineNumber=stop.get('LineNumber')
    if stopID in stopDict:
        # append stopLineNumber to line list in dictionary
        stopDict[stopID].get('')
        stopDict.update(stopID:)
    if stopID not in stopDict:
        stopDict[stopID] = {'lon':null,'lat':null,'line':[stop.get('LineNumber')]}
    
        stopDict.update(stopID:)

    


#for stop in stopsAndLines:
#    if locationOfStops[stop.get('StopPointNumber')]
#    graphData.update({stop.get('StopPointNumber') : {'lon':stop.get('LocationEastingCoordinate'),'lat':stop.get('LocationNorthingCoordinate')}})
#
#for stop in result2:
#    graphData.update({stop.get('JourneyPatternPointNumber') : {'line':[stop.get('LineNumber')]}})
