import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import logging
from shapely.geometry import Point, Polygon
import numpy as np

# Konfigurace loggeru
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Načtení GeoJSON zelených ploch ze souboru
logger.info("Načítání prvního GeoJSON souboru.")
gdf1 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/vyznamne_plochy_zelene.geojson")
logger.info("První GeoJSON soubor načten.")

# Načtení GeoJSON stromů ze souboru
logger.info("Načítání druhého GeoJSON souboru.")
gdf2 = gpd.read_file("/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/stromy_kere_2014_2024.geojson")
logger.info("Druhý GeoJSON soubor načten.")

# Vytvoření bodového GeoDataFrame
logger.info("Vytváření bodového GeoDataFrame.")
points = gpd.GeoDataFrame(geometry=[Point(1847613.3149919452, 6308942.125034717),
                                     Point(1846431.9702917489, 6303486.735041085),
                                     Point(1848647.6289087017, 6309926.419632995),
                                     Point(1856633.2216363496, 6296883.781669727)],
                           crs=gdf2.crs)  # Převzít souřadnicový systém z gdf2

# Vytvoření polygonů o kruhovém tvaru kolem bodů
logger.info("Vytváření polygonů o kruhovém tvaru.")
circles = []
for point in points.geometry:
    x, y = point.x, point.y
    angles = np.linspace(0, 2 * np.pi, 20)  # 20 vrcholů
    polygon_points = [(x + np.cos(angle) * 700, y + np.sin(angle) * 700) for angle in angles]  # Poloměr 1 km
    circles.append(Polygon(polygon_points))

# Vytvoření GeoDataFrame pro polygony
circles_gdf = gpd.GeoDataFrame(geometry=circles, crs=gdf2.crs)

# Vytvoření grafu
logger.info("Vytváření grafu.")
fig, ax = plt.subplots(figsize=(10, 5))

# Vykreslení zelených ploch
logger.info("Vykreslování zelených ploch.")
gdf1.plot(ax=ax, color='palegreen', alpha=0.3, edgecolor='green', label='Zelené plochy', aspect=1)

# Vykreslení stromů
logger.info("Vykreslování stromů.")
gdf2.plot(ax=ax, color='seagreen', alpha=0.5, label='Stromy', markersize=2, aspect=1)

# Vykreslení polygonů
logger.info("Vykreslování polygonů.")
circles_gdf.plot(ax=ax, color='none', edgecolor='blue', alpha=0.5)

# Vykreslení bodů
logger.info("Vykreslování bodů.")
points.plot(ax=ax, color='blue', markersize=5, label='Merici stanice')

# Přidání podkladové mapy pomocí OpenStreetMap
logger.info("Přidávání podkladové mapy.")
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

# Zobrazení legendy
logger.info("Přidání legendy.")
plt.legend()

# Uložení grafu do souboru PNG s vysokým rozlišením
logger.info("Ukládání grafu do souboru PNG.")
plt.savefig("/Users/mirus/Desktop/python/PROJEKT/python-projekt/vysledky/plot_high_res.png", dpi=300)
logger.info("Graf uložen jako plot_high_res.png.")

# Zobrazení grafu
logger.info("Zobrazení grafu.")
plt.show()
logger.info("Skript dokončen.")
