s#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:04:00 2020

@author: nebelschwaden
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "/home/nebelschwaden/Documents/2020A/PythonGR1/py-jaramillo-rojas-ronny-xavier/ProyectoScrapy/arania_mod/arania_mod/spiders/movies.csv"
columnas = ['movie_name', 'release_date', 'country', 'runtime', 'rating', 
            'genre', 'imdb_rating', 'imdb_votes', 'tmdb_rating', 'tmdb_votes']

df = pd.read_csv(
    path,
    usecols = columnas)

#for pie
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%\n({v:d})'.format(p=pct,v=val)
    return my_autopct

# movies por año
unique_year = df['release_date'].str.split(",\s",2).str[1]
por_year = unique_year.value_counts().head(15)
por_year = por_year.sort_index()
por_year.plot(kind='bar')
# movies por mes
unique_month = df['release_date'].str.split(".",2).str[0]
por_month = unique_month.value_counts()
cats = ['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']
por_month.index = pd.CategoricalIndex(por_month.index, categories=cats, ordered=True)
por_month = por_month.sort_index()
fig, ax = plt.subplots()
ax.plot(por_month.index, por_month.values) 
plt.show()
# movies por rating
por_rating = df['rating'].value_counts().head(10)
pie_3 = plt.figure(figsize=(18,15))
plt.pie(por_rating.values,labels=por_rating.index,autopct=make_autopct(por_rating.values))
plt.show()
# top 10 paises con mas peliculas
por_country = df['country'].value_counts().head(10)
por_country.plot(kind='barh')
#top 15 movies con mayor runtime
por_runtime = df[['movie_name','runtime']]
por_runtime['runtime'] = por_runtime['runtime'].str.split("\s",2).str[0]
por_runtime['runtime'] = por_runtime['runtime'].apply(pd.to_numeric)
por_runtime = por_runtime.sort_values(by=['runtime'], ascending=False)
por_runtime = por_runtime.head(15)
bar = plt.figure()
ax = bar.add_axes([0,0,1,1])
ax.bar(por_runtime['movie_name'],por_runtime['runtime'])
plt.xticks(rotation='vertical')
plt.show()
#top 10 paises con menos peliculas
por_country_l = df['country'].value_counts().tail(10)
por_country_l.plot(kind='barh')
#top 15 movies con menor runtime
por_runtime_l = df[['movie_name','runtime']]
por_runtime_l['runtime'] = por_runtime_l['runtime'].str.split("\s",2).str[0]
por_runtime_l['runtime'] = por_runtime_l['runtime'].apply(pd.to_numeric)
por_runtime_l = por_runtime_l.sort_values(by=['runtime'], ascending=True).iloc[30:]
por_runtime_l = por_runtime_l.head(15)
bar = plt.figure()
ax = bar.add_axes([0,0,1,1])
ax.bar(por_runtime_l['movie_name'],por_runtime_l['runtime'])
plt.xticks(rotation='vertical')
plt.show()
#top 5 genres con mas peliculas
por_genre = df['genre'].value_counts().drop(labels=['Actualizadas'])
por_genre = por_genre.head(5)
pie_3 = plt.figure(figsize=(15,12))
plt.pie(por_genre.values,labels=por_genre.index,autopct=make_autopct(por_genre.values))
plt.show()
#top 5 genres con menos peliculas
por_genre_l = df['genre'].value_counts().drop(labels=['Actualizadas'])
por_genre_l = por_genre_l.tail(5)
pie_3 = plt.figure(figsize=(14,11))
plt.pie(por_genre_l.values,labels=por_genre_l.index,autopct=make_autopct(por_genre_l.values))
plt.show()
#top 15 peliculas con mayor imdb_rating
por_imdb_rat = df[['movie_name','imdb_rating']].sort_values(by=['imdb_rating'], ascending=False).head(15)
fig, ax = plt.subplots()
ax.plot(por_imdb_rat['movie_name'], por_imdb_rat['imdb_rating'])
plt.xticks(rotation='vertical')
plt.show()
#top 15 peliculas con mayor imdb_votes
por_imdb_vo = df[['movie_name','imdb_votes']].sort_values(by=['imdb_votes'],ascending=False).iloc[1:]
por_imdb_vo['imdb_votes'] = por_imdb_vo['imdb_votes'].str.replace(',','')
por_imdb_vo['imdb_votes'] = por_imdb_vo['imdb_votes'].apply(pd.to_numeric)
por_imdb_vo = por_imdb_vo.sort_values(by=['imdb_votes'], ascending=False).head(15)
bar = plt.figure()
ax = bar.add_axes([0,0,1,1])
ax.bar(por_imdb_vo['movie_name'],por_imdb_vo['imdb_votes'])
plt.xticks(rotation='vertical')
plt.show()
#top 15 peliculas con menor imdb_rating
por_imdb_rat_l = df[['movie_name','imdb_rating']].sort_values(by=['imdb_rating'], ascending=False).tail(68).iloc[:15]
fig, ax = plt.subplots()
ax.plot(por_imdb_rat_l['movie_name'], por_imdb_rat_l['imdb_rating'])
plt.xticks(rotation='vertical')
plt.show()
#top 15 peliculas con menor imdb_votes
por_imdb_vo_l = df[['movie_name','imdb_votes']].sort_values(by=['imdb_votes'],ascending=False).iloc[1:]
por_imdb_vo_l['imdb_votes'] = por_imdb_vo_l['imdb_votes'].str.replace(',','')
por_imdb_vo_l['imdb_votes'] = por_imdb_vo_l['imdb_votes'].apply(pd.to_numeric)
por_imdb_vo_l = por_imdb_vo_l.sort_values(by=['imdb_votes'], ascending=False).tail(68).iloc[:15]
bar = plt.figure()
ax = bar.add_axes([0,0,1,1])
ax.bar(por_imdb_vo_l['movie_name'],por_imdb_vo_l['imdb_votes'])
plt.xticks(rotation='vertical')
plt.show()
#top 15 peliculas con mayor tmdb_rating
por_tmdb_rat = df[['movie_name','tmdb_rating']].sort_values(by=['tmdb_rating'], ascending=False).head(15)
fig, ax = plt.subplots()
ax.plot(por_tmdb_rat['movie_name'], por_tmdb_rat['tmdb_rating'])
plt.xticks(rotation='vertical')
plt.show()
#top 15 peliculas con mayor tmdb_votes
por_tmdb_vo = df[['movie_name','tmdb_votes']].sort_values(by=['tmdb_votes'],ascending=False)
por_tmdb_vo['tmdb_votes'] = por_tmdb_vo['tmdb_votes'].str.replace(',','')
por_tmdb_vo['tmdb_votes'] = por_tmdb_vo['tmdb_votes'].apply(pd.to_numeric)
por_tmdb_vo = por_tmdb_vo.sort_values(by=['tmdb_votes'], ascending=False).head(15)
bar = plt.figure()
ax = bar.add_axes([0,0,1,1])
ax.bar(por_tmdb_vo['movie_name'],por_tmdb_vo['tmdb_votes'])
plt.xticks(rotation='vertical')
plt.show()
#top 15 peliculas con menor tmdb_rating
por_tmdb_rat_l = df[['movie_name','tmdb_rating']].sort_values(by=['tmdb_rating'], ascending=False).tail(144).iloc[:15]
fig, ax = plt.subplots()
ax.plot(por_tmdb_rat_l['movie_name'], por_tmdb_rat_l['tmdb_rating'])
plt.xticks(rotation='vertical')
plt.show()
#top 15 peliculas con menor tmdb_votes
por_tmdb_vo_l = df[['movie_name','tmdb_votes']].sort_values(by=['tmdb_votes'],ascending=False)
por_tmdb_vo_l['tmdb_votes'] = por_tmdb_vo_l['tmdb_votes'].str.replace(',','')
por_tmdb_vo_l['tmdb_votes'] = por_tmdb_vo_l['tmdb_votes'].apply(pd.to_numeric)
por_tmdb_vo_l = por_tmdb_vo_l.sort_values(by=['tmdb_votes'], ascending=False).tail(747).iloc[:15]
fig, ax = plt.subplots()
ax.plot(por_tmdb_vo_l['movie_name'], por_tmdb_vo_l['tmdb_votes'])
plt.xticks(rotation='vertical')
plt.show()
#top 15 países cuyas películas tienen el mayor número de imdb_votes acumulado
por_count_vo = df[['country','imdb_votes']].sort_values(by=['imdb_votes'],ascending=False)[1:]
por_count_vo['imdb_votes'] = por_count_vo['imdb_votes'].str.replace(',','')
por_count_vo['imdb_votes'] = por_count_vo['imdb_votes'].apply(pd.to_numeric)
prv = por_count_vo.groupby('country')['imdb_votes'].sum()
prv = prv.sort_values(ascending=False).head(15)
bar = plt.figure()
ax = bar.add_axes([0,0,1,1])
ax.bar(prv.index,prv.values)
plt.xticks(rotation='vertical')
plt.show()
#top 15 países cuyas películas tienen el menor número de imdb_votes acumulado
prvl = por_count_vo.groupby('country')['imdb_votes'].sum()
prvl = prvl.sort_values(ascending=False).tail(15)
bar = plt.figure()
ax = bar.add_axes([0,0,1,1])
ax.bar(prvl.index,prvl.values)
plt.xticks(rotation='vertical')
plt.show()
#top 15 países cuyas películas tienen el mayor número de tmdb_votes acumulado
por_count_vo_tm = df[['country','tmdb_votes']].sort_values(by=['tmdb_votes'],ascending=False)[1:]
por_count_vo_tm['tmdb_votes'] = por_count_vo_tm['tmdb_votes'].str.replace(',','')
por_count_vo_tm['tmdb_votes'] = por_count_vo_tm['tmdb_votes'].apply(pd.to_numeric)
prvt = por_count_vo_tm.groupby('country')['tmdb_votes'].sum()
prvt = prvt.sort_values(ascending=False).head(15)
bar = plt.figure()
ax = bar.add_axes([0,0,1,1])
ax.bar(prvt.index,prvt.values)
plt.xticks(rotation='vertical')
plt.show()
#top 15 países cuyas películas tienen el menor número de tmdb_votes acumulado
prvtl = por_count_vo_tm.groupby('country')['tmdb_votes'].sum()
prvtl = prvtl.sort_values(ascending=False).tail(15)
bar = plt.figure()
ax = bar.add_axes([0,0,1,1])
ax.bar(prvtl.index,prvtl.values)
plt.xticks(rotation='vertical')
plt.show()