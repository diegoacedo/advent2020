#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:06:23 2020

@author: hazedo
"""

import pandas as pd
import ast

data = open('inputday4.txt')

contents = data.read()

listacambios=list()

#Localizador de los separadores. 

for i in range(0,len(contents)):
    if contents[i] == '\n' and contents[i+1]=='\n':
        listacambios.append(i)
        
#Entradas expresadas como listas
listadiccionarios = [contents[0:70]]

for i in range(1,len(listacambios)):
  listadiccionarios.append(contents[(listacambios[i-1]+2):listacambios[i]])
    
listadiccionarios.append(contents[listacambios[i]+2:])
    
#Separación de cada lista

for i in range(0,len(listadiccionarios)):
    listadiccionarios[i]=listadiccionarios[i].split()

#Actividad 1

ctr = 0
listavalidos= list()
for i in range(0,len(listadiccionarios)):
    ok=0
    if len(listadiccionarios[i])==8:
            ctr = ctr+ 1
            listavalidos.append(listadiccionarios[i])
    if len(listadiccionarios[i])==7:
        for j in listadiccionarios[i]:
            if j.find('cid')==-1: ok +=1
        if ok == 7: 
            ctr = ctr+1
            listavalidos.append(listadiccionarios[i])
                
print('resultado=', ctr)

#Actividad 2

ok=1
for j in listavalidos[0]:

    if find('byr') != -1:
        
        

    
    
    



            
    

        
 