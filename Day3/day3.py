#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:16:46 2020

@author: hazedo
"""

import numpy as np
import pandas as pd

#Importar datos 
data = pd.read_csv('inputday3.txt',sep = '\n',header=None)
matrix = data.values.tolist()

#Actividad 1

derecha=0
lfila= len(matrix[0][0])
ntrees=0

for alt in range(1, len(matrix)):
    derecha = (derecha + 3) % lfila
    if matrix[alt][0][derecha] == '#':
        ntrees=ntrees+1
        
print(ntrees)

#Actividad 2

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
resultados = list()

for i in range(0,len(slopes)):
    derecha=slopes[i][0]
    bajada=slopes[i][1]
    vert = 0
    horiz = 0
    ntrees = 0
    while vert <= len(matrix)-bajada-1:
        vert = vert + bajada
        horiz = (horiz + derecha) % lfila
        if matrix[vert][0][horiz] == '#':
            ntrees=ntrees+1
    resultados.append(ntrees)

print(np.prod(resultados))
        


