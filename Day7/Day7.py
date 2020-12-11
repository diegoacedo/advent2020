#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:50:11 2020

@author: hazedo
"""

import pandas as pd
import numpy as np

data = pd.read_csv('inputday7.txt', sep='\n',header=None)

sents = data.values.tolist()

sents = [sents[i][0] for i in range(0, len(sents))]


containers = [sents[i].split(sep=" contain")[0][0:-5] for i in range(0,len(sents))]

containees = [sents[i].split(sep=" contain ")[1] for i in range(0,len(sents))]

containees = [containees[i].split(sep=", ") for i in range(0, len(sents))]

#Dividimos según cada número:
for i in range(0, len(containees)):
    for j in range(0,len(containees[i])):
        if containees[i][j]!="no other bags.":
            containees[i][j] =[
                containees[i][j][0],
                containees[i][j][2:]
                ]
        else: containees[i][j]=['0', containees[i][j]]
        
"""
for i in range(0, len(sents)):
    for k in range(0,len(containees[i])):
        if containees[i][k] == "no other bags." and len(containees[i])>1:
            containees[i] = containees[i].remove(containees[i][k])
"""

#Reemplazamos bags por bag 
for i in range(0, len(containees)):
    containees[i][-1][1]=containees[i][-1][1].replace(".","")
    for k in range(0, len(containees[i])):
        containees[i][k][1]=containees[i][k][1].replace("bags","bag")
        containees[i][k][1] = containees[i][k][1][0:-4]
    
    
        
colors = list()


#List of colors.

for i in range(0,len(containers)):
    color = containers[i]
    if color not in colors: colors.append(color)
 
#for i in range(0, len(containees)):   
#    for k in range(0, len(containees[i])):
#        color = containees[i][k][2:-4]
#        if color not in colors: colors.append(color)

matrix=[]

for i in range(0, len(colors)):
    lista = list()
    for j in range(0, len(containees)):
        for k in range(0, len(containees[j])):
            if containees[j][k][1].find(colors[i]) != -1:
                lista.append(containers[j])
    matrix.append(lista)

inicio = colors.index("shiny gold")

listashiny=["shiny gold"]

def ncontenedores(contenido):
    i = colors.index(contenido)
    for j in range(0,len(matrix[i])):
        if matrix[i][j] not in listashiny:
            listashiny.append(matrix[i][j])
            ncontenedores(matrix[i][j])

ncontenedores("shiny gold")

print("Resultado actividad 1 = ",len(listashiny)-1)

#Actividad 2

numcontenidos=0


def ncontenidos(contenedor):
    i = colors.index(contenedor)
    sumatotal=0
    lista=list()
    for j in range(0,len(containees[i])):
        suma=0
        if containees[i][j][0] != '0': #si contiene alguna mochila.   
            suma = int(containees[i][j][0])*(1+ncontenidos(containees[i][j][1]))        
        lista.append(suma)

    return(sum(lista))

resultado = ncontenidos("shiny gold")
print("Resultado actividad 2 = ",resultado)
        