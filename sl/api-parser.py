# -*- coding: utf-8 -*-

import requests
import json
    
api_response1 = requests.get('http://api.sl.se/api2/LineData.json?model=stoppoint&key=461aca8d48264b3f9a3f31d701fce8f8')
api_response2 = requests.get('http://api.sl.se/api2/LineData.json?model=JourneyPatternPointOnLine&key=461aca8d48264b3f9a3f31d701fce8f8')

locationOfStops = api_response1.json().get('ResponseData').get('Result')
stopsAndLines = api_response2.json().get('ResponseData').get('Result')

stopDict = {"1337":{"lon":1,"lat":2}}

for stop in locationOfStops:
    stopDict[stop.get('StopPointNumber')] = {'name':stop.get('StopPointName'),'lon':stop.get('LocationEastingCoordinate'),'lat':stop.get('LocationNorthingCoordinate'),'lineList':[]}
    
for stop in stopsAndLines:
    
    stopID=stop.get('JourneyPatternPointNumber')
    stopLineNumber=stop.get('LineNumber')
    
    if stopID in stopDict:
        # append stopLineNumber to lineList for each existing stopDict with same key in dictionary
        stopDict[stopID].get('lineList').append(stopLineNumber)
    if stopID not in stopDict:
        # create new dictionary entry with stopID as key and the linenumber
        stopDict[stopID] = {'lon':'null','lat':'null','lineList':[stop.get('LineNumber')]}