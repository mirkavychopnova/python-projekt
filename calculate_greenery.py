import geopandas as gpd
from shapely.geometry import Point
import pandas as pd

def calculate_green_percentage(coordinates_list, green_file_path, trees_file_path):
    # Načtení GeoJSON souborů
    stromy_kere_df = gpd.read_file(trees_file_path)
    vyznamne_plochy_df = gpd.read_file(green_file_path)

    results = []

    for coords in coordinates_list:
        # Definování centrálního bodu s danými souřadnicemi
        central_point = Point(coords)

        # Vytvoření bufferu o poloměru 700 m kolem centrálního bodu
        buffer = central_point.buffer(700)

        # Výběr stromů, které jsou uvnitř bufferu nebo se s ním dotýkají
        stromy_in_buffer = stromy_kere_df[stromy_kere_df.distance(buffer) <= 700]

        # Počet stromů v bufferu
        num_trees_in_buffer = len(stromy_in_buffer)

        # Výběr ploch zeleně, které se protínají s bufferem
        vyznamne_plochy_in_buffer = vyznamne_plochy_df[vyznamne_plochy_df.intersects(buffer)]

        # Výpočet celkové plochy bufferu
        total_area = buffer.area

        # Výpočet celkové plochy zeleně v bufferu
        if not vyznamne_plochy_in_buffer.empty:
            green_area = vyznamne_plochy_in_buffer.unary_union.intersection(buffer).area
        else:
            green_area = 0

        # Výpočet procenta zelené plochy
        percent_green_area = (green_area / total_area) * 100

        # Výsledek
        result = {
            'coordinates': coords,
            'green_percentage': percent_green_area,
            'num_trees_in_buffer': num_trees_in_buffer
        }

        # Přidání výsledku do seznamu
        results.append(result)

    # Vytvoření DataFrame z výsledků
    results_df = pd.DataFrame(results)

    return results_df

# Seznam souřadnic, pro které chcete spočítat procento zeleně
coordinates_list = [
    (1847613.3149919452, 6308942.125034717),
    (1846431.9702917489, 6303486.735041085),
    (1848647.6289087017, 6309926.419632995),
    (1856633.2216363496, 6296883.781669727)
]

# Cesta k GeoJSON souboru se zelenými plochami
green_file_path = '/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/vyznamne_plochy_zelene.geojson'

# Cesta k GeoJSON souboru se stromy
trees_file_path = '/Users/mirus/Desktop/python/PROJEKT/python-projekt/souradnice/stromy_kere_2014_2024.geojson'

# Výpočet procenta zeleně pro zadané souřadnice
results = calculate_green_percentage(coordinates_list, green_file_path, trees_file_path)

# Zobrazení výsledků
print(results)

# Cesta k souboru, do kterého budeme ukládat výsledky
output_file_path = '/Users/mirus/Desktop/python/PROJEKT/python-projekt/vysledky/zastoupeni_zelene.csv'

# Uložení výsledků do souboru
results.to_csv(output_file_path, sep=',', index=False)

print(f"Výsledky byly uloženy do souboru: {output_file_path}")
