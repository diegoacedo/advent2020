#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:02:47 2020

@author: hazedo
"""
 
import pandas as pd

data = pd.read_csv('inputday5.txt', sep='\n',header=None)

passports = data.values.tolist()

passports = [passports[i][0] for i in range(0,len(passports))] #row

#passports2 = [passports[i][0][7:10] for i in range(0,len(passports))] #column


longrow = 2**7
longcolumn = 2**3
rowlist=list()
collist = list()

#Actividad 1

for i in range(0,len(passports)):
    
    intervalrmin = 0
    intervalrmax = longrow
    
    intervalcmin = 0
    intervalcmax = longcolumn
    
    for j in range(0,6):
        if passports[i][j] == 'F': 
            intervalrmax = intervalrmax - (intervalrmax - intervalrmin)/2
        else:
            intervalrmin = intervalrmin + (intervalrmax - intervalrmin)/2
            
    if passports[i][6] == 'F': rowlist.append(intervalrmin)
    else: rowlist.append(intervalrmax-1)
    
    for j in range(7,9):
        if passports[i][j] == 'L': 
            intervalcmax = intervalcmax - (intervalcmax - intervalcmin)/2
        else:
            intervalcmin = intervalcmin + (intervalcmax - intervalcmin)/2
            
    if passports[i][9] == 'L': collist.append(intervalcmin)
    else: collist.append(intervalcmax-1)
    
idlist = [rowlist[i]*8 + collist[i] for i in range(0,len(passports))]

print(max(idlist))

#Actividad 2

idlist.sort()

for i in range(0,len(idlist)-1):
    if idlist[i+1] != idlist[i]+1:
        print(idlist[i]+1)


