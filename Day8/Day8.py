#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:41:21 2020

@author: hazedo
"""

import pandas as pd

data = pd.read_csv('inputday8.txt', header=None)

data = data.values.tolist()

data = [data[i][0].split() for i in range(0,len(data))] 

acc=0
j=0

def funcion (contents):
    i=0
    acc=0
    listai=[]
    
    while i not in listai and i < 654:
        
        listai.append(i)
        
        if contents[i][0] == 'acc' :
            acc += int(contents[i][1])
            i += 1
        
        else:
            if contents[i][0] == 'jmp':
                i += int(contents[i][1])
        
            else:
                i += 1
    
    return(i,acc)
      

#índices de jmp y nop

listajmp = list()
listanop = list()

for k in range(0,len(data)):
    if data[k][0] == 'jmp':
        listajmp.append(k)
    if data[k][0] == 'nop':
        listanop.append(k)

#Comprobamos qué ocurre si cambiamos un jmp por un nop
for k in listajmp:
    newdata=[]
    newdata = copy.deepcopy(data)
    newdata[k][0] = 'nop'
    index, account = funcion(newdata)
    if index >= 654: print(' Jmp to nop.\n','Index =',k,'\n Account =',account)

#Comprobamos qué ocurre si cambiamos un nop por un jmp
for k in listanop:
    newdata=[]
    newdata = copy.deepcopy(data)
    newdata[k][0] = 'jmp'
    index, account = funcion(newdata)
    if index >= 654: print(' Nop to jmp.\n','Index =',k,'\n Account =',account)
