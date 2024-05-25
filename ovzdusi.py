import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Cesta k souboru
file_path = '/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/kvalita_ovzdusi_2.csv'

# Načtení dat ze souboru
df = pd.read_csv(file_path)

# Převod sloupce Datum na datetime
df['Datum'] = pd.to_datetime(df['Datum'])

# Filtr na měsíce 5, 6, 7, 8, 9 roku 2022
months_filter = df['Datum'].dt.month.isin([5, 6, 7, 8, 9])
year_filter = df['Datum'].dt.year == 2022
df = df[months_filter & year_filter]

# Převod na GeoDataFrame
geometry = [Point(xy) for xy in zip(df.X, df.Y)]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Zadané souřadnice
coords = [
    (1847613.3149919452, 6308942.125034717),
    (1846431.9702917489, 6303486.735041085),
    (1848647.6289087017, 6309926.419632995),
    (1856633.2216363496, 6296883.781669727)
]

# Vytvoření GeoDataFrame z těchto souřadnic
coord_gdf = gpd.GeoDataFrame(geometry=[Point(x, y) for x, y in coords])

# Seznam ukazatelů
indicators = ['PM10', 'PM2_5', 'NO_', 'NO2', 'Nox', 'O3', 'SO2', 'CO', 'RychlostVetru', 'Vlhkost']

# Tolerance pro filtrování (700 metrů)
tolerance = 700  # tolerance in meters

# Výsledek
results = []

for coord in coords:
    # Filtrování dat pro aktuální souřadnici
    filtered_gdf = gdf[gdf.geometry.apply(lambda x: x.distance(Point(coord)) <= tolerance)]
    
    # Agregace dat podle měsíce
    filtered_gdf['Month'] = filtered_gdf['Datum'].dt.month
    monthly_means = filtered_gdf.groupby('Month')[indicators].mean().reset_index()
    
    # Přidání souřadnic do výsledků
    monthly_means['X'] = coord[0]
    monthly_means['Y'] = coord[1]
    
    results.append(monthly_means)

# Spojení všech výsledků do jednoho DataFrame
final_result = pd.concat(results)

print(final_result)

