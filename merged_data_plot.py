import os
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import logging

# Konfigurace loggeru
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Vyčištění terminálu
os.system('clear')
logger.info("Terminál byl vyčištěn.")

# Načtení prvního GeoJSON ze souboru
logger.info("Načítání prvního GeoJSON souboru.")
gdf1 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/vyznamne_plochy_zelene.geojson")
logger.info("První GeoJSON soubor načten.")

# Načtení druhého GeoJSON ze souboru
logger.info("Načítání druhého GeoJSON souboru.")
gdf2 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/stromy_kere_2014_2024.geojson")
logger.info("Druhý GeoJSON soubor načten.")

# Načtení třetího GeoJSON ze souboru
logger.info("Načítání třetího GeoJSON souboru.")
gdf3 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/teplota_nespojita_prevedena.geojson")
logger.info("Třetí GeoJSON soubor načten.")

# Vytvoření nového grafu
logger.info("Vytváření grafu.")
fig, ax = plt.subplots(figsize=(10, 5))

# Vykreslení zelených ploch
logger.info("Vykreslování zelených ploch.")
gdf1.plot(ax=ax, color='palegreen', alpha=0.3, label='Zelené plochy', aspect=1)

# Vykreslení stromů
logger.info("Vykreslování stromů.")
gdf2.plot(ax=ax, color='seagreen', alpha=0.5, label='Stromy', markersize=5, aspect=1)

# Vykreslení pozice měřících stanic
logger.info("Vykreslování pozic měřících stanic.")
gdf3.plot(ax=ax, color='red', alpha=0.5, label='Měřící stanice', markersize=7, aspect=1)

# Přidání podkladové mapy pomocí OpenStreetMap
logger.info("Přidávání podkladové mapy.")
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

# Zobrazení legendy
logger.info("Přidání legendy.")
plt.legend()

# Uložení grafu do souboru PNG s vysokým rozlišením
logger.info("Ukládání grafu do souboru PNG.")
plt.savefig("/Users/mirus/Desktop/python/PROJEKT/python-projekt/plot_high_res.png", dpi=300)
logger.info("Graf uložen jako plot_high_res.png.")

# Zobrazení grafu
# logger.info("Zobrazení grafu.")
# plt.show()
logger.info("Skript dokončen.")
