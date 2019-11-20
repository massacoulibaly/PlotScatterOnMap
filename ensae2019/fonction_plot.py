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
        qu'on souhaite projeter (ici, on se limite uniquement aux coordonnées de France)
    """
    ax.set_extent(limit)
    ax.add_feature(cfeature.OCEAN.with_scale('50m'))
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
    ax.add_feature(cfeature.RIVERS.with_scale('50m'))
    ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')

def nom_ville(ax , x, y, name):
    for i, txt in enumerate(name):
        ax.text(x[i]+0.1, y[i]+0.1, txt, fontsize=9)



def plot_geo_time_value(x, y, year, value, axs=None, hue='', **kwargs):
    """
    Visualise l'évolution temporelle d'une donnée numérique
    géolocalisée sur plusieurs graphiques.

    :param x: longitudes (vecteur)
    :param y: latitudes (vecteur)
    :param year: années (vecteur)
    :param value: valeurs numériques à représenter (DataFrame ou numpy array de taille n_observations * n_years)
    :param axs: axes matplotlib sur lesquels tracer (vecteur ou numpay array)
    :param hue: sens de la valeur numérique (:math:`CO_2`, Ammoniac, ...)
    :param kwargs: paramètres additionnels
    """ 
    # Vérification du type de years
    if type(year) != list:
        raise TypeError("Le paramètre years doit être une liste!")
    # vérification du type de values
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

        
    # Définition des variables et affectations
    nrow = np.array(axs).shape[0]
    ncol = np.array(axs).shape[1]
    i=0
    j=0
    lim_metropole = [-5, 10, 41, 52]

    for k, an in enumerate(year) :
        if i < nrow :
            if j < ncol :
                ax0 = axs[(i,j)]
                axe_projection(ax=ax0, limit=lim_metropole)
                if type(value) == pd.DataFrame:
                    ax0.scatter(x, y, s=value.iloc[:,k] ** 0.6 / 5, alpha=0.5,
                                zorder = 10, transform=ccrs.PlateCarree())
                elif type(value) == np.array:
                    ax0.scatter(x, y, s=value[:,k] ** 0.6 / 5, alpha=0.5,
                                zorder = 10, transform=ccrs.PlateCarree())
                ax0.set_title('France ' +str(an)+ '\n'+ hue);
                j = j+1
            else:
                if i < nrow-1:
                    i = i+1
                j=0
                ax0 = axs[(i,j)]
                axe_projection(ax=ax0, limit=lim_metropole)
                if type(value) == pd.DataFrame:
                    ax0.scatter(x, y, s=value.iloc[:,k] ** 0.6 / 5, alpha=0.5,
                            zorder = 10, transform=ccrs.PlateCarree())
                elif type(value) == np.array:
                    ax0.scatter(x, y, s=value[:,k] ** 0.6 / 5, alpha=0.5,
                            zorder = 10, transform=ccrs.PlateCarree())
                ax0.set_title('France ' +str(an)+ '\n'+ hue);
                j = j+1
    plt.savefig("graph.pdf")

