import pandas as pd
import numpy as np
import urllib.request
import zipfile
from tqdm import tqdm
from pyproj import Proj, transform
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
import matplotlib.animation as animation


def axe_projection(ax = None,limit = None):
    """
        param ax: type axe sur lequel sera projeté la carte de la région concernée
        param limit: liste contenant les coordonnées (latitude et longitude) de la région 
                        qu'on souhaite projeter
    """
    ax.set_extent(limit)
    ax.add_feature(cfeature.OCEAN.with_scale('50m'))
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
    ax.add_feature(cfeature.RIVERS.with_scale('50m'))
    ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')

def nom_ville(ax , x, y, name):
    for i, txt in enumerate(name):
        ax.text(x[i]+0.1, y[i]+0.1, txt, fontsize=9)



def plot_geo_time_value_gif(x, y, year, value, fig = None, axs=None, hue='', **kwargs):
    """
    Visualise l'évolution temporelle d'une donnée numérique
    géolocalisée sous forme d'une animation et enregistre un 
    fichier gif (nommé graph.gif) dans le repertoire de travail.

    :param x: longitudes (vecteur)
    :param y: latitudes (vecteur)
    :param year: années (vecteur)
    :param value: valeurs numériques à représenter (DataFrame ou numpy array de taille n_observations * n_years)
    :param axs: axes matplotlib sur lesquels tracer (vecteur ou numpay array)
    :param hue: sens de la valeur numérique (:math:`CO_2`, Ammoniac, ...)
    :param kwargs: paramètres additionnels
    """ 
    lim_metropole = [-5, 10, 41, 52]

    if type(year) != list:
        raise TypeError("Le paramètre years doit être une liste!")
    
    if type(value) not in [np.array, pd.DataFrame]:    
        raise TypeError("Le paramètre value doit être de type array ou un DataFrame!")
        
    if type(value) == np.array:
        for col in range(value.shape[1]):
            if list(filter(lambda x : x<0, value[:,col])) !=  []:
                raise ValueError("La taille des points ne peut pas être négative!")
                break
    else:
        for col in range(np.array(value).shape[1]):
            if list(filter(lambda x : x<0, value.iloc[:,col])) !=  []:
                raise ValueError("La taille des points ne peut pas être négative!")
                break

    if fig == None:
        fig,axs = plt.subplots(figsize=(20,20), subplot_kw={'projection': ccrs.Mercator()})
    axe_projection(ax=axs,limit = lim_metropole)

    if type(value) == pd.DataFrame:
        scat = axs.scatter(x, y, s=value.iloc[:,0] ** 0.6 / 5, alpha=0.5,
                    zorder = 10, transform=ccrs.PlateCarree())
    elif type(value) == np.array:
        scat = axs.scatter(x, y, s=value[:,0] ** 0.6 / 5, alpha=0.5,
                    zorder = 10, transform=ccrs.PlateCarree())
    
    # Fonction animate qui permet de mettre à jour le graph
    def animate(i):
        if type(value) == pd.DataFrame:
            scat.set_sizes(sizes = value.iloc[:,year.index(i)] ** 0.6 / 5)
            axs.set_title('France ' +str(i)+ '\n'+ hue);
        elif type(value) == np.array:
            scat.set_sizes(sizes = value[:,year.index(i)] ** 0.6 / 5)
            axs.set_title('France ' +str(i)+ '\n'+ hue);
        return scat,
    
    anim = FuncAnimation(fig,animate, frames=year,repeat=True, interval = 1000, blit=True)
    plt.show()
    anim.save('graph.gif', writer = "pillow")
