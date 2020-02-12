#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API key: 270394d8f8c74e5191d4f235e8dd925e
"""

# -*- coding: utf-8 -*-

import requests
import json

gtfs_static_ul = requests.get('https://opendata.samtrafiken.se/ul/ul.zip?key=270394d8f8c74e5191d4f235e8dd925e')

data = gtfs_static_ul.json()

