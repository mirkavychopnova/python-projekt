import json
import logging
from pyproj import Proj, Transformer

# Konfigurace loggeru
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Definuj projekci pro vstupní (zeměpisné) souřadnice
input_proj = Proj('epsg:4326')  # WGS 84 (zeměpisný)

# Definuj projekci pro výstupní (projektované) souřadnice
output_proj = Proj('epsg:3857')  # WGS 84 / Pseudo-Mercator

# Vytvoření transformátoru
transformer = Transformer.from_proj(input_proj, output_proj)

# Načíst GeoJSON soubor
logger.info("Načítání GeoJSON souboru.")
with open('/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/kvalita_ovzdusi.geojson', 'r') as f:
    data = json.load(f)
logger.info("GeoJSON soubor načten.")

# Pro každou vlastnost v GeoJSON souboru
logger.info("Převod souřadnic zahájen.")
for feature in data['features']:
    # Získání zeměpisných souřadnic
    longitude, latitude = feature['geometry']['coordinates']
    
    # Převeď zeměpisné souřadnice na souřadnice projektované
    x, y = transformer.transform(latitude, longitude)  # Pozor na pořadí souřadnic
    
    # Nahraď původní zeměpisné souřadnice novými projektovanými souřadnicemi
    feature['geometry']['coordinates'] = [x, y]
logger.info("Převod souřadnic ukončen.")

# Ulož upravený GeoJSON soubor
logger.info("Ukládání nového souboru.")
with open('/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/kvalita_ovzdusi_prevedena.geojson', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
logger.info("Nový soubor uložen.")
