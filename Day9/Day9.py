#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:38:28 2020

@author: hazedo
"""

import pandas as pd
import numpy as np

data = pd.read_csv('inputday9.txt',sep='\n')

data = data.values.tolist()

data = [data[i][0] for i in range(0,len(data))]


#Activity 1
sol = 0
active = data[0:25]
ctr=25

def comprob(lista,n):
    ok = 0
    for i in range(0,len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]+lista[j] == n: ok = 1
    
    return ok


while sol == 0:

    if comprob(active, data[ctr]) == 0: 
        sol = data[ctr] 
        
    active.remove(active[0])
    active.append(data[ctr])
    ctr = ctr + 1


#Activity 2

invalidnumber = sol
sol2 = 0

for length in range(10, 511):
    
    for i in range(0, len(data) - length):
        suma = sum(data[i:i+length])
        if suma == invalidnumber: 
            sol2 = min(data[i:i+length]) + max(data[i:i+length])
        if suma > invalidnumber: 
            break
        
    
