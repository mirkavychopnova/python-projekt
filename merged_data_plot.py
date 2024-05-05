import os
import geopandas as gpd
import matplotlib.pyplot as plt

# Vyčištění terminálu
os.system('clear')

# Načtení prvního GeoJSON ze souboru
gdf1 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/vyznamne_plochy_zelene.geojson")

# Načtení druhého GeoJSON ze souboru
gdf2 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/stromy_kere_2014_2024.geojson")

# TODO převést GPS formát do POLYGON formátu
# Načtení třetího GeoJSON ze souboru
# gdf3 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/teplota_nespojita.geojson")

# Vykreslení prvního GeoDataFrame
plt.figure(figsize=(10, 5))
gdf1.plot(ax=plt.gca(), color='palegreen', alpha=0.5, label='Zelené plochy')

# Vykreslení druhého GeoDataFrame
gdf2.plot(ax=plt.gca(), color='seagreen', alpha=0.7, label='Stromy', markersize=10)

# Vykreslení třetího GeoDataFrame
# gdf3.plot(ax=plt.gca(), color='red', alpha=0.7, label='Teploty', markersize=10)

# Zobrazení legendy
# plt.legend()

plt.show()
