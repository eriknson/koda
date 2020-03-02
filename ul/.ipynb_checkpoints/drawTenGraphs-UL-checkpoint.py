#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.offline import plot

edgeList = []
locDict = {}
graphObject = nx.DiGraph()

#for x, routeID in enumerate(routeStations.keys()):
#    if x<15:
#        for (i,stop) in enumerate(routeStations[routeID]['stops']):
#            if i+1 < len(routeStations[routeID]['stops']):
#                edgeList.append((routeStations[routeID]['stops'][i]['stop_id'], 
#                         routeStations[routeID]['stops'][i+1]['stop_id']))


for stop in graphObject.nodes():
    print(stops[stop])

# Create edgeList
for routeID in routeStations.keys():
    for (i,stop) in enumerate(routeStations[routeID]['stops']):
        if i+1 < len(routeStations[routeID]['stops']):
            edgeList.append((routeStations[routeID]['stops'][i]['stop_id'], 
                     routeStations[routeID]['stops'][i+1]['stop_id']))

# Create edges (and nodes) for each edge in list
for edge in edgeList:
    graphObject.add_edge(edge[0],edge[1],weight=1)

# Create locDict with key for each node and value as (lon,lat)
for node in graphObject.nodes():
    locDict[node]=(stops[node]['stop_lon'],stops[node]['stop_lat'])
   
edge_x = []
edge_y = []
for edge in edgeList:
    x0, y0 = (stops[edge[0]]['stop_lon'],stops[edge[0]]['stop_lat'])
    x1, y1 = (stops[edge[1]]['stop_lon'],stops[edge[1]]['stop_lat'])
    
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')


node_x = []
node_y = []
for node in graphObject.nodes():
    x, y = (stops[node]['stop_lon'],stops[node]['stop_lat'])
    node_x.append(x)
    node_y.append(y)
    
node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))
        
        
node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(graphObject.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
                     
for i, node_id in enumerate(graphObject.nodes()):
    node_text.append(stops[node_id]['stop_name'] + ' ' + str(stops[node_id]['stop_id']))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text

fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Uppsala Public Transport Network',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
plot(fig, auto_open=True)


    
