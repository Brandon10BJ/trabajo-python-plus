from collections import Counter
import csv
from pathlib import Path

# Ruta absoluta del archivo
ruta = Path('C:/Users/suare/OneDrive/Escritorio/trabajo de python plus/dataset/songs_normalize.csv')

def my_function(file_name, n=None):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            artists = Counter(map(lambda x: x[0], reader))
            if n is not None:    
                return artists.most_common(n)
            else:
                return artists.most_common(10)  # Si no se especifica, devuelve los 10 más comunes
    except FileNotFoundError:
        print("¡Tenemos un problema! El archivo no se encuentra en la ruta especificada.")

# Llamada a la función con la ruta
my_songs = my_function(ruta)

# Imprimir los resultados
if my_songs:
    for song in my_songs:
        print(song)
