import pandas as pd
import geojson
from collections import defaultdict

# Načtení geojson souboru
with open('/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/kvalita_ovzdusi_prevedena.geojson', 'r') as f:
    data = geojson.load(f)

# Extrahování vlastností a souřadnic
features = data['features']

# Inicializace datové struktury pro ukládání dat
data_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

# Procházení funkcí a sběr dat
for feature in features:
    props = feature['properties']
    coords = tuple(feature['geometry']['coordinates'])
    month = pd.to_datetime(props['actualized']).month
    if month in [5, 6, 7, 8, 9]:
        for attr in ["so2_1h", "no2_1h", "co_8h", "pm10_1h", "o3_1h", "pm10_24h", "pm2_5_1h"]:
            value = props[attr]
            if value is not None:
                data_dict[coords][month][attr].append(float(value))

# Výpočet statistik
stats = []
for coords, month_values in data_dict.items():
    for month, attr_values in month_values.items():
        row = {'Coordinates': coords, 'Month': month}
        # Načtení názvu místa z geojson
        for feature in features:
            if tuple(feature['geometry']['coordinates']) == coords:
                row['Place Name'] = feature['properties']['name']
                break
        # Přidání statistik atributů
        for attr, values in attr_values.items():
            series = pd.Series(values)
            row[attr] = {
                'mean': series.mean()
                # 'std': series.std(),
                # 'min': series.min(),
                # 'max': series.max()
            }
        stats.append(row)

# Vytvoření DataFrame a uložení do CSV
df = pd.DataFrame(stats)
df.to_csv('/Users/mirus/Desktop/python/PROJEKT/python-projekt/vysledky/kvalita_ovzdusi.csv', index=False)
