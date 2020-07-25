#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:34 2020

@author: nebelschwaden
"""

import numpy as np
import pandas as pd
lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(lista_numeros)

series_b = pd.Series(tupla_numeros)

series_c = pd.Series(np_numeros)

series_d = pd.Series(
    [True,
    False,
    12,
    12.12,
    "Adrian",
    (1),
    [2],
    {"noombre": "Ronny"}])

print(series_d[3])

lista_ciudades = ["Ambato","Loja","Cuenca","Quito"]

serie_ciudad = pd.Series(lista_ciudades,
                         index = ["A","C","L","Q"])

print(serie_ciudad[2])
print(serie_ciudad["Q"])

valores_ciudad = {
    "Ibarra":9500,
    "Guayaquil":10000,
    "Cuenca":7000,
    "Quito":8000,
    "Loja":3000}

serie_valor_ciudad = pd.Series(valores_ciudad)

ciudades_menor_5k = serie_valor_ciudad < 5000

print(type(serie_valor_ciudad))
print(type(ciudades_menor_5k))
print(ciudades_menor_5k)

serie_valor_ciudad = serie_valor_ciudad * 1.1
serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

print("Lima" in serie_valor_ciudad)

svc_cuadrado = np.square(serie_valor_ciudad)

ciudades_uno = pd.Series({
    "Montañita":300,
    "Guayaquil":3000,
    "Quito":2000})
ciudades_dos = pd.Series({
    "Loja":300,
    "Guayaquil":3000})

ciudades_uno["Loja"]=0

print(ciudades_uno + ciudades_dos)
print(type(ciudades_uno + ciudades_dos))

ciudades_add = ciudades_uno.add(ciudades_dos)
# sub(), mult(), div()

ciudad_concat = pd.concat([
    ciudades_uno,
    ciudades_dos])

ciud_concat_verify = pd.concat([
    ciudades_uno,
    ciudades_dos],
    verify_integrity = False)

ciud_concat_verify = ciudades_uno.append(
    ciudades_dos,
    verify_integrity = False)

print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))
print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))

print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))

print(ciudades_uno.head(2))
print(ciudades_uno.tail(2))

print(ciudades_uno.sort_values(
    ascending = False).head(2))

def calcular(valor_serie):
    if(valor_serie < 1000):
        return valor_serie * 1.05
    elif(valor_serie > 1000 and valor_serie <= 5000):
        return valor_serie * 1.10
    elif(valor_serie > 5000):
        return valor_serie * 1.15

ciudad_calculada = ciudades_uno.map(calcular)

#IF ELSE
#CUANDO NO CUMPLE CON LA CONDICIÓN, SE APLICA
resultado = ciudades_uno.where(ciudades_uno < 1000, ciudades_uno * 1.05)


series_numeros = pd.Series(['1.0','2',-3])
print(pd.to_numeric(series_numeros))

print(pd.to_numeric(series_numeros,downcast='integer'))

series_numeros_err = pd.Series(['no tiene','1.0','2',-3])

#Ignore, Coerce, raise (default)
#print(pd.to_numeric(series_numeros_err))
print(pd.to_numeric(series_numeros_err, errors='ignore'))
print(pd.to_numeric(series_numeros_err,errors='coerce'))