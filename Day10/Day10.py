#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:42:29 2020

@author: hazedo
"""

import pandas as pd

#Obtain data

data = pd.read_csv("inputday10.txt", header=None)

data = data.values.tolist()

data = [data[i][0] for i in range(0,len(data))]

#We add the first and last adapters

data.append(0)
data.append(max(data)+3)

data.sort() #Yeah, you are right, there is probably a more efficient way but this kinda works.

#Activity 1

listadiferencias = [0,0,0] 

for i in range(1,len(data)):
    dif = data[i]-data[i-1]
    if dif == 2:
        print(i)
    listadiferencias[dif-1] +=1 


result = (listadiferencias[2])*(listadiferencias[0]) 

print('Resultado1 = ', result)

#Activity 2

listadiferencias = []
length = len(data)

for i in range(0,length-3):
    listadiferencias.append([data[i+1]-data[i],data[i+2]-data[i],data[i+3]-data[i]])
  
#We add 4 as last differences to solve any inconveniences and keep the indices correct.
listadiferencias.append([data[-2]-data[-3],data[-1]-data[-3],4])
listadiferencias.append([data[-1]-data[-2],4,4])
listadiferencias.append([4,4,4])

listanwaystocount=[0 for i in range(0,len(data))]
listanwaystocount[-1] = 1
    
for k in range(2,len(data)+1):
    i = len(data)-k
    suma = 0
    suma += listanwaystocount[i+1]
    if listadiferencias[i][1] <= 3: 
        suma+= listanwaystocount[i+2]
    if listadiferencias[i][2] <= 3: 
        suma+= listanwaystocount[i+3]
    listanwaystocount[i] = suma

print('Resultado2 = ', listanwaystocount[0])