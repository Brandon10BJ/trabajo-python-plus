from collections import Counter
import csv
from pathlib import Path

ruta = ruta_absoluta = Path('C:/Users/suare/OneDrive/Escritorio/trabajo de python plus/dataset/songs_normalize.csv')
ruta_archivo = Path('.') / 'datasets' / 'songs_normalize.csv'
def my_function(file_name, n=None):
     with open(file_name, 'r',encoding='utf-8') as file:
         reader = csv.reader(file, delimiter=',')
         artists = Counter(map(lambda x: x[0], reader))
     if n is not None:    
         return artists.most_common(n)
     else :
         return artists.most_common(10)#pongo 10 a modo de ejeplo sino me muestra todo el dataset

try:
    my_songs = my_function(ruta)
except FileNotFoundError:
    print("Tenemos un problema!!")
finally:
     for song in my_songs:
         print(song)
        