import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
# Načtení dat z CSV souboru
csv_file = "/Users/mirus/Desktop/python/PROJEKT/python-projekt/teploty/brno_teploty_2022.csv"
df = pd.read_csv(csv_file, delimiter=';')

# Zobrazení názvů sloupců pro ověření
print(df.columns)

# Převedení sloupce 'Souřadnice' na seznamy [x, y]
df['Souřadnice'] = df['Souřadnice'].apply(lambda x: tuple(map(float, x.split(','))))

# Vytvoření GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=df['Souřadnice'].apply(lambda coords: Point(coords)), crs='EPSG:3857')

# Uložení do GeoJSON
geojson_file = "/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/merici_stanice.geojson"
gdf.to_file(geojson_file, driver='GeoJSON')

print(f"CSV soubor byl úspěšně převeden na GeoJSON a uložen do {geojson_file}.")