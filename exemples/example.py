# -*- coding: utf-8 -*-
"""
@author: Sandra, Massa, Cheick

"""
###########################################################################################################
#                                                                                                         #
#                             Importation des modules utilisés                                            #
#                                                                                                         #
###########################################################################################################     

from fonction_plot import plot_geo_time_value 
from fonction_plot_gif import plot_geo_time_value_gif
from fonction_plot_mp4 import plot_geo_time_value_mp4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from tqdm import tqdm
from pyproj import Proj, transform
############################################################################################################
#                                                                                                          #
#                                       Programme principal                                                #
#                                                                                                          #
############################################################################################################

""" 
Dans cet exemple, nous utilisons le module que nous avons créé, afin de représenter les émissions polluantes 
des entreprises collectées par le Bureau de recherches géologiques et minières (BRGM) sur plusieurs années. 
Nous allons nous intéresser aux données de 2003 à 2017. Les données sont disponibles sur leur site internet 
Ces données ont été téléchargées et enregistrées dans un fichier csv 'dataset' qui se trouve dans le répertoire

"""

#                                       Etape 1 : chargement des données                                   #
############################################################################################################    


df_metro = pd.read_csv('dataset.csv')
x, y = df_metro['LLX'], df_metro['LLY'] #  y=latitude, x=Longitude


#         Etape 2 : représentation des emissions polluantes en France de 2004 à 2007 en mosaïque           #
############################################################################################################


years = range(2004, 2008)
years_str = [str(year) for year in years] # transformer chaine de caractère 
values = df_metro[[colname for colname in df_metro.columns.values if colname[-4:] in years_str]].astype('float') 
# on se limite aux emissions polluantes de 2004 à 2007 et changement du type 
years = list(np.arange(2003,2008))
#♠ Le Subplot permet d’organiser les différents tracés à l’intérieur d’une grille d’affichage.
"""fig, axs = plt.subplots(2,2,figsize=(20,20), subplot_kw={'projection': ccrs.Mercator()}) 
# On voudrait une grille contenant deux colonnes et deux lignes pour les quatres années à représenter 
# le figsize renseigne la taille de la grille
# le système de projection utilisé est le Mercator qui améliore l'affichage

plot_geo_time_value(x=x,y=y,year=years,value=values,axs=axs,hue='Emissions polluantes') """
# x: longitudes, y: latitudes, year: années à représenter, value: valeurs numériques à représenter, 
# axs: axes matplotlib sur lesquels tracer, hue: sens de la valeur numérique

"""
A l'issu de cette étape, on peut apercevoir à l'écran quatre graphiques. 
La taille des points est une fonction croissante de la quantité d'émissions polluantes
Globalement de 2004 à 2007, il y a croissance des quantités d'émissions polluantes. 
On peut aussi ajouter qu'il y a plus d'émissions dans le Nord de la France

Le graphique est sauvegardé dans le fichier "graphe.pdf" au niveau du répertoire
"""
 
#        Etape 3 : représentation des émissions polluantes en France de 2003 à 2017 sous format gif        #
############################################################################################################

# Chargement des données
years = range(2003, 2018)
years_str = [str(year) for year in years] # transformer chaine de caractère 
values = df_metro[[colname for colname in df_metro.columns.values if colname[-4:] in years_str]].astype('float')

years = list(np.arange(2003,2018))

fig, axs = plt.subplots(figsize=(20,20), subplot_kw={'projection': ccrs.Mercator()}) 
# pour cette représentation, on a pas besoin de partitionner la grille d'affichage comme dans le cas précédent

plot_geo_time_value_gif(x=x,y=y,year=years,value=values,axs=axs, fig=fig, hue='Emissions polluantes')  
# x: longitudes, y: latitudes, year: années à représenter, value: valeurs numériques à représenter, 
# axs: axes matplotlib sur lesquels tracer, hue: sens de la valeur numérique
"""
Le gif est sauvegardé sous le nom 'graph.gif' dans le répertoire
le constat fait précédemment sur l'évolution des émissions polluantes reste le même jusqu'en 2017.  

"""

#      Etape 4 : représentation des émissions polluantes en France de 2003 à 2017 sous format mp4          #
############################################################################################################

'''
Avant d'executer le code ci-dessuous, il faut d'abord installer la librairie de ffmepg 
    
'''

fig, axs = plt.subplots(figsize=(20,20), subplot_kw={'projection': ccrs.Mercator()}) 
# De même que pour le gif, on a pas besoin de partitionner la grille

# les années et valeurs sont identiques à celles du Gif donc on ne refait plus les même étapes

plot_geo_time_value_mp4(x=x,y=y,year=years,value=values,axs=axs,fig=fig, hue='Emissions polluantes')
# x: longitudes, y: latitudes, year: années à représenter, value: valeurs numériques à représenter, 
# axs: axes matplotlib sur lesquels tracer, hue: sens de la valeur numérique 

"""
La vidéo mp4 est sauvegardée sous le nom 'graph.mp4' dans le répertoire courant

"""


############################################################################################################    
#                                                                                                          #
#                                          Fin du Programme                                                #
#                                                                                                          #
############################################################################################################
