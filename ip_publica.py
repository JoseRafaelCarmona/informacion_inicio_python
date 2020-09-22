# inicio para requests
import requests
from bs4 import BeautifulSoup

def obtener_ip_publica():
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
    url = 'https://www.cual-es-mi-ip.net/'  
    contenido_pagina = requests.get(url, headers)
    soup = BeautifulSoup(contenido_pagina.text, 'html.parser')
    return str(soup.find("span", {"class": "big-text font-arial"}).getText())