#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:13:29 2020

@author: hazedo
"""

import pandas as pd
import ast

data = open('inputday6.txt')

contents = data.read()

listacambios=list()

#Localizador de los separadores. 

for i in range(0,len(contents)):
    if contents[i] == '\n' and contents[i+1]=='\n':
        listacambios.append(i)
        
#Entradas expresadas como listas
listagrupos = [contents[0:6]]

for i in range(1,len(listacambios)):
    listagrupos.append(contents[(listacambios[i-1]+2):listacambios[i]])
    
listagrupos.append(contents[listacambios[i]+2:])

listagrupos2 = [listagrupos[i] for i in range(0, len(listagrupos))]

#Actividad 1

#Eliminar los saltos
for i in range(0, len(listagrupos)):
   listagrupos[i]=listagrupos[i].replace("\n",'')
        
sizes = []
for i in range(0,len(listagrupos)):
    lista = []
    for j in listagrupos[i]:
        if j not in lista: lista.append(j)
    sizes.append(len(lista))
    
print(sum(sizes))

#Actividad 2


for i in range(0,len(listagrupos2)):
    listagrupos2[i]=listagrupos2[i].split()

sizes2 = []
for i in range(0, len(listagrupos2)):
    lista = []
    for j in listagrupos2[i][0]:
        ctr = 0 
        for k in range(1,len(listagrupos2[i])):
            if j in listagrupos2[i][k]:ctr +=1 
        if ctr ==len(listagrupos2[i])-1: lista.append(j)
    sizes2.append(len(lista))
        
print(sum(sizes2))
