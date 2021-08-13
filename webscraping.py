
from bs4 import BeautifulSoup as BS
import csv
import requests

# Libros

url_cuspide='https://www.cuspide.com/cienmasvendidos' # url final
respuesta=requests.get(url_cuspide)
respuesta.encoding='utf-8'
html_cuspide=respuesta.text
dom=BS(html_cuspide,features='html.parser')
libros = dom.find_all('article')

# Precios

url_cuspide_precios = 'https://www.cuspide.com/'
precios_href = libros[0].figure.div.a['href']
url_precios = url_cuspide_precios + precios_href # url final
respuesta_precio = requests.get(url_precios)
respuesta_precio.encoding = 'utf-8'
html_precio = respuesta_precio.text
dom_precio = BS(html_precio, features='html.parser')
precios = dom_precio.find_all('meta', itemprop="price")

# tabla

tabla = [['Posicion', 'Libro', 'Precio ARS']]

# for

conteo = 0
for libro in libros:
    fila_libros = libro.figure.div.a['title']
    conteo += 1
    url_cuspide_precios = 'https://www.cuspide.com/'
    precios_href = libro.figure.div.a['href']
    url_precios = url_cuspide_precios + precios_href
    respuesta_precio = requests.get(url_precios)
    respuesta_precio.encoding = 'utf-8'
    html_precio = respuesta_precio.text
    dom_precio = BS(html_precio, features='html.parser')
    precios = dom_precio.find_all('meta', itemprop="price")
    for precio in precios:
        precios_finales = precio['content']
        fila = [conteo, fila_libros, precios_finales]
        tabla.append(fila)
        print(conteo,'-->', fila_libros,'-->', precios_finales)

# guardar csv

with open('librosprecios.csv', 'w', newline = '') as file:
    salida = csv.writer(file)
    salida.writerows(tabla)
    

    
  