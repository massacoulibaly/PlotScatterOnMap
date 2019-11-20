# Nom de la fonction test_plot_geo_time_value
import unittest
from ensae2019.fonction_plot import plot_geo_time_value
import pandas as pd
import matplotlib.pyplot as plt
from pyproj import Proj, transform
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.animation import FuncAnimation 
import matplotlib.animation as animation

years = [2000, 2001]
x = [-2,1,1.3,2,5]
y = [45,45.3,46,49,47.5]
value = pd.DataFrame(data = [[10,11],
                             [17, 14],
                             [3,17],
                             [5,13],
                             [11,5]], columns = ['Quantite2000','Quantite2001'])
value_1 = pd.DataFrame(data = [[-10,11],
                             [17,- 14],
                             [3,17],
                             [-5,13],
                             [11,-5]], columns = ['Quantite2000','Quantite2001'])

fig, axs = plt.subplots(1,1,figsize=(20,20), subplot_kw={'projection': ccrs.Mercator()}) 

class TestPlotGeoTimeValue(unittest.TestCase):
    def test_type_years(self):
        #Test le type de l'argument years de la fonction (years doit être une liste)
        self.assertRaises(TypeError, plot_geo_time_value, x, y, True, value,axs, hue='Test')
        self.assertRaises(TypeError, plot_geo_time_value,x, y, "years", value,axs, hue='Test')
        self.assertRaises(TypeError, plot_geo_time_value, x, y, 1, value,axs, hue='Test')
        
    def test_valeur_values(self):
        #On s'assure qu'une ValueError est envoyé quand c'est nécessaire
        self.assertRaises(ValueError, plot_geo_time_value, x, y, years, value_1,axs, hue='Test')
        

if __name__ == '__main__':
    unittest.main()