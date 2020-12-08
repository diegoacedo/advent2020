#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:51:19 2020

@author: hazedo
"""

import pandas as pd

data = pd.read_csv('inputday2.txt',sep = '\n',header=None)

#Recuperación de los datos
lista = data.values.tolist()

data_list = list()
for sublist in lista:
    for item in sublist:
        data_list.append(item)
    
#Actividad 1

#Estructura de la información.
posguiones = list()
posespacio = list()

leng = len(data_list)

#Definición de mínimos y máximos.     
for i in range(0,leng):
    posguiones.append(data_list[i].find('-'))
    posespacio.append(data_list[i].find(' '))
    
minimos = list()

for i in range(0,leng):
    if posguiones[i] == 1:
        minimos.append(int(data_list[i][0]))
    else:
        minimos.append(int(data_list[i][0:2]))

maximos = list()    
    
for i in range(0,leng):
    if posguiones[i] == 1:
        if posespacio[i] == 3:
            maximos.append(int(data_list[i][2]))
        else:
            maximos.append(int(data_list[i][2:4]))
    else:
        if posespacio[i] == 4:
            maximos.append(int(data_list[i][3]))
        else:
            maximos.append(int(data_list[i][3:5]))

letrasclave = [data_list[i][posespacio[i]+1] for i in range(0,leng)]

passwords = [data_list[i][posespacio[i]+4:len(data_list[i])] for i in range(0,leng)]

#Actividad 1
correctpasswords = list()

for i in range(0,leng):
    letra = letrasclave[i]
    password = passwords[i]
    minimo = minimos[i]
    maximo = maximos[i]
    contador = 0
    for j in password:
        if j == letra:
            contador=contador+1
    if minimo <= contador and contador <= maximo: 
        correctpasswords.append(i)
        
print(len(correctpasswords))
        

#Actividad 2

correctpasswords2 = list()

for i in range(0,leng):
    letra = letrasclave[i]
    password = passwords[i]
    pos1 = minimos[i]-1
    pos2 = maximos[i]-1
    long =len(password)
    if pos1 < long and pos2 <= long:
        if (password[pos1] == letra)^(password[pos2] == letra):
            correctpasswords2.append(i)

print(len(correctpasswords2))
