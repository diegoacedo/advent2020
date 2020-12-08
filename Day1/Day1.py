#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:16:30 2020

@author: hazedo
"""

import pandas as pd

lista = pd.read_csv('inputday1.txt')

lista = lista.values.tolist()

#flatten la lista

flat_list = list()
for sublist in lista:
    for item in sublist:
        flat_list.append(item)
    

#Actividad 1
listaresultados = list()
for i in range(0,len(flat_list)):
    for j in range(i+1,len(flat_list)): 
        if flat_list[i] + flat_list[j] == 2020: 
            listaresultados.append([flat_list[i],flat_list[j],flat_list[i]*flat_list[j]])

#Actividad 2

listaresultados2 = list()
for i in range(0,len(flat_list)):
    for j in range(i+1,len(flat_list)): 
        for k in range(i+j+1, len(flat_list)):
            if flat_list[i] + flat_list[j] + flat_list[k] == 2020: 
                listaresultados2.append([flat_list[i],flat_list[j],flat_list[k],flat_list[i]*flat_list[j]*flat_list[k]])
