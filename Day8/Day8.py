#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:41:21 2020

@author: hazedo
"""

import pandas as pd

data = pd.read_csv('inputday8.txt', header=None)

contents = data.values.tolist()

contents = [contents[i][0].split() for i in range(0,len(contents))] 

acc=0

i = 0
j=0
listai = []

while i not in listai:
        
   listai.append(i)
        
   if contents[i][0] == 'acc':
      acc += int(contents[i][1])
      i += 1
        
   if contents[i][0] == 'jmp':
      i += int(contents[i][1])
        
   if contents[i][0] == 'nop':
      i += 1
