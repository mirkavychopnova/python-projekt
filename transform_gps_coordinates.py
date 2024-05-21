import json
from pyproj import Proj, transform

# Definuj projekci pro vstupní (zeměpisné) souřadnice
input_proj = Proj(init='epsg:4326')  # WGS 84 (zeměpisný)

# Definuj projekci pro výstupní (projektované) souřadnice
output_proj = Proj(init='epsg:3857')  # WGS 84 / UTM zone 33N

# Načíst GeoJSON soubor
with open('/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/teplota_nespojita.geojson', 'r') as f:
    data = json.load(f)

# Pro každou vlastnost v GeoJSON souboru
for feature in data['features']:
    # Získání zeměpisných souřadnic
    longitude, latitude = feature['geometry']['coordinates']
    
    # Převeď zeměpisné souřadnice na souřadnice projektované
    x, y = transform(input_proj, output_proj, longitude, latitude)
    
    # Nahraď původní zeměpisné souřadnice novými projektovanými souřadnicemi
    feature['geometry']['coordinates'] = [x, y]

# Ulož upravený GeoJSON soubor
with open('/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/teplota_nespojita_prevedena.geojson', 'w') as f:
    json.dump(data, f, indent=4)
