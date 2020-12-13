#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:12:56 2020

@author: hazedo
"""

import pandas as pd
import numpy as np

data = pd.read_csv("Day12input.txt", header= None)

data = data.values.tolist()

mov = [data[i][0][0] for i in range(0,len(data))]

length = [int(data[i][0][1:]) for i in range(0,len(data))]

#Initial position 

east = 0
north = 0
orientorder = ['E','S','W','N']
orientation = 0 #starts looking east.
nsteps = len(data)


def goeast(size,e,n):
    return e + size, n

def gowest(size,e,n):
    return e-size, n

def gonorth(size,e,n):
    return e,n+size

def gosouth(size,e,n):
    return e, n-size

movements = [goeast,gosouth,gowest,gonorth]


for i in range(0,nsteps):
    if mov[i] == 'L':
        orientation = (orientation -int(length[i]/90))%4 #we turn -length degrees
    
    if mov[i] == 'R':
        orientation = (orientation + int(length[i]/90))%4
    
    if mov[i] == 'F':
        east, north = movements[orientation](length[i],east,north)
    
    if mov[i] == 'N':
        east, north = gonorth(length[i],east,north)

    if mov[i] == 'E':
        east, north = goeast(length[i],east,north)
        
    if mov[i] == 'S':
        east, north = gosouth(length[i],east,north)
        
    if mov[i] == 'W':
        east, north = gowest(length[i],east,north)
        
print ('Solution 1=',abs(east)+ abs(north))
        

#Activity 2

east = 0
north = 0
weast  = 10
wnorth = 1

def turnleft(e,n,ndeg):
    if ndeg == 90:
        return -n,e
    
    if ndeg == 180:
        return -e,-n
    
    if ndeg == 270:
        return n,-e
    

for i in range(0,nsteps):    
    if mov[i] == 'L':
        weast,wnorth = turnleft(weast,wnorth,length[i])
    
    if mov[i] == 'R':
        weast,wnorth = turnleft(weast,wnorth, 360-length[i])
    
    if mov[i] == 'F':
        east += length[i]*weast
        north += length[i]*wnorth
        
    if mov[i] == 'N':
        weast, wnorth = gonorth(length[i],weast,wnorth)

    if mov[i] == 'E':
        weast, wnorth = goeast(length[i],weast,wnorth)

    if mov[i] == 'S':
        weast, wnorth = gosouth(length[i],weast,wnorth)
        
    if mov[i] == 'W':
        weast, wnorth = gowest(length[i],weast,wnorth)


print('Solution 2=', abs(east)+abs(north))
