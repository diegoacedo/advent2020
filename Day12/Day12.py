#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:12:56 2020

@author: hazedo
"""

import pandas as pd

data = pd.read_csv("Day12input.txt")

data = data.values.tolist()

mov = [data[i][0][0] for i in range(0,len(data))]

length = [data[i][0][1:] for i in range(0,len(data))]