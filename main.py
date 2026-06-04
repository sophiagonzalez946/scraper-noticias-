from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv


url = "https://books.toscrape.com/"

res = requests.get(url)
if res.status_code != 200:
 print("error al acceder", res.status_code)
 exit()

soup = BeautifulSoup(res.text, "html.parser")

titulos = soup.find_all("h3")
precios = soup.find_all("p", class_ = "price_color")
libros = soup.find_all("article", class_ ="product_pod")

with open("libros.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["titulo", "precio","enlace","punto"])

    for titulo, precio, libroC in zip(titulos, precios,libros):
     enlace = titulo.find("a")
     nombre = enlace["title"]
     url_l = enlace["href"]
     costo = precio.text

     rating_tag = libroC.find("p", class_="star-rating")
     puntuacion = rating_tag["class"][1]
     url_c = urljoin(url, url_l)
     escritor.writerow([nombre,costo, url_c, puntuacion])
    
     print(nombre)
     print(costo)
     print(url_c)
     print(puntuacion)
     print("-" * 30)
