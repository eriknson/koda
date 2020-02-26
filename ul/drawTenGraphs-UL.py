#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:36:13 2020

@author: axelboman
"""

import networkx as nx
import matplotlib.pyplot as plt

central_routes = ['9011001059300000', '9011001099500000', '9011003000600000', '9011003001100000', 
                  '9011003010000000', '9011003010800000', '9011003011900000', '9011003080100000', 
                  '9011003088000000', '9011003089600000', '9011003099900000']

two_routes = ['9011003001100000', '9011003000600000']

edgeList = []
locDict = {}
graphObject = nx.DiGraph()

def build_edge_list():    
    for routeID in two_routes:
        for (i,stop) in enumerate(routes[routeID]):
            if i+1 < len(routes[routeID]):
                edgeList.append((routes[routeID][i]['stop_id'], 
                         routes[routeID][i+1]['stop_id']))
    
build_edge_list()

for edge in edgeList:
    graphObject.add_edge(edge[0],edge[1])

for node in graphObject.nodes():
    locDict[node]=(stops[node]['stop_lon'],stops[node]['stop_lat'])
    
plt.figure(figsize=(10,15))


nx.draw(graphObject, with_labels=True)


    
