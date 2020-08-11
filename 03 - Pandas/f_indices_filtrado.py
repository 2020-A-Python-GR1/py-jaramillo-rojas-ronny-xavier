#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:32:39 2020

@author: nebelschwaden
"""

import pandas as pd

path_guardado = "/home/nebelschwaden/Documents/2020A/PythonGR1/py-jaramillo-rojas-ronny-xavier/03 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(type(artistas)) #Numpy Array

blake = df['artist'] == 'Blake, William' #Serie
print(blake.value_count())
res= df[blake]
