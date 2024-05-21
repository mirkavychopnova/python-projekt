import os
import geopandas as gpd
import matplotlib.pyplot as plt

# Vyčištění terminálu
os.system('clear')

# Načtení prvního GeoJSON ze souboru
gdf1 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/vyznamne_plochy_zelene.geojson")

# Načtení druhého GeoJSON ze souboru
gdf2 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/stromy_kere_2014_2024.geojson")

# Načtení třetího GeoJSON ze souboru
gdf3 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/teplota_nespojita_prevedena.geojson")
gdf4 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/test.geojson")

# Vytvoření nového grafu
plt.figure(figsize=(10, 5))
ax = plt.gca()

# Vykreslení prvního GeoDataFrame
gdf1.plot(ax=ax, color='palegreen', alpha=0.5, label='Zelené plochy', aspect=1)

# Vykreslení druhého GeoDataFrame
gdf2.plot(ax=ax, color='seagreen', alpha=0.7, label='Stromy', markersize=10, aspect=1)

# Vykreslení třetího GeoDataFrame
gdf3.plot(ax=ax, color='red', alpha=0.7, label='Teploty', markersize=10, aspect=1)

gdf4.plot(ax=ax, color='blue', alpha=0.7, label='Test', aspect=1)

# Zobrazení legendy
plt.legend()

# Zobrazení grafu
plt.show()
