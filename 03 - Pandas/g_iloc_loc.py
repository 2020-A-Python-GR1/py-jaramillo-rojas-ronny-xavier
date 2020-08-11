#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:34 2020

@author: nebelschwaden
"""


import pandas as pd

path_guardado = "/home/nebelschwaden/Documents/2020A/PythonGR1/py-jaramillo-rojas-ronny-xavier/03 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

#Para obtener un registro en específico (toda una fila)
#Toda la fila del índice 1035
filtrado_horizontal = df.loc[1035]
# Sólo columna artist la fila del artista 'blake'  del índice 1035
filtrado_horizontal['artist']
#Indices columnas
filtrado_horizontal.index

#Filtrar columnas
serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index)

#FIltrar por indice (True & False)
df_1035 = df[df.index==1035]

#Múltiples registros
segundo = df.loc[[1035,1036]]

#Filtrando desde x indice hasta y indice (sin ordenar, obtendrá más registros
# de los que se quiere)
segundo_2 = df.loc[3:5]

#Múltiples columnas específicas
segundo = df.loc[1035,'artist']# 1 indice
segundo = df.loc[1035,['artist','medium']]

#ILOC
#Acceder grupo filas y columnas indices en 0
tercero = df.iloc[0]

tercero = df.iloc[[0,1]]

tercero = df.iloc[0:10]

tercero = df.iloc[df.index == 1035]

#Filtrando indices por rango de indice 0:4
tercero = df.iloc[0:10, 0:4]