# Folium es una biblioteca de Python que permite crear mapas interactivos en un navegador web,
# aprovechando la potencia de Leaflet.js (una librería de JavaScript para mapas).
# Con ella se pueden representar puntos, rutas, áreas y distintos tipos de datos geográficos.

# Instalamos la librería (solo se hace una vez desde la terminal o consola):
# pip install folium

# Importamos la biblioteca folium para poder usar sus funciones y clases.
import folium 

# Creamos un objeto de mapa centrado en unas coordenadas específicas.
# En este caso, las coordenadas corresponden a Buenos Aires, Argentina.
# location = [-34.6037, -58.3816]  -> latitud y longitud del punto central del mapa.
# zoom_start = 12  -> nivel de acercamiento inicial (cuanto mayor el número, más zoom).
mapa = folium.Map(location=[-34.6037, -58.3816], zoom_start=12)

# Guardamos el mapa generado en un archivo HTML llamado "map.html".
# Este archivo se puede abrir en cualquier navegador y mostrará el mapa interactivo.
mapa.save("map.html")
