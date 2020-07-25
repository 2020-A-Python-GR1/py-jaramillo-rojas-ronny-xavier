#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:08:03 2020

@author: nebelschwaden
"""
import pandas as pd
import os

path = "/home/nebelschwaden/Documents/2020A/PythonGR1/py-jaramillo-rojas-ronny-xavier/03 - Pandas/data/artwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows=10)

columnas = ['id','artist','title','medium','year','acquisitionYear','height','width','units']

df2 = pd.read_csv(
    path,
    nrows = 10,
    usecols = columnas)

df3 = pd.read_csv(
    path,
    nrows = 10,
    usecols = columnas,
    index_col='id')

path_guardado = "/home/nebelschwaden/Documents/2020A/PythonGR1/py-jaramillo-rojas-ronny-xavier/03 - Pandas/data/artwork_data.pickle"

df3.to_pickle(path_guardado)

df5 = pd.read_pickle(path_guardado)