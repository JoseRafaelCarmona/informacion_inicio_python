from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from subprocess import Popen, PIPE, STDOUT
import os
#prueba con los colores#
from colorama import Fore, init, Back, Style

BIENVENIDA = '''
 ______  _                             _     _       
(____  \(_)                           (_)   | |      
 ____)  )_  ____ ____ _   _ ____ ____  _  _ | | ___  
|  __  (| |/ _  )  _ \ | | / _  )  _ \| |/ || |/ _ \ 
| |__)  ) ( (/ /| | | \ V ( (/ /| | | | ( (_| | |_| |
|______/|_|\____)_| |_|\_/ \____)_| |_|_|\____|\___/ 
'''

WEBDRIVER_PATH = '/opt/chromedriver'

def definir_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(WEBDRIVER_PATH,options=options)
    return driver

def buscar_ip_publica(driver):
    driver.get('https://www.cual-es-mi-ip.net/')
    ip_address = driver.find_element_by_xpath('//*[@id="ip-col"]/span')
    return ip_address.text
 
def comando(orden):
    eventStatus = Popen(orden, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    outputStatus = eventStatus.communicate()
    return outputStatus[0].decode('utf-8')

def salida_datos(ip_publica,ip_privada):
    print(Fore.GREEN+'Tu direccion ip publica>> '+ Fore.WHITE+'%s'%ip_publica)
    print(Fore.GREEN+'Tu direccion ip privada>> '+ Fore.WHITE+'%s'%ip_privada)

if __name__ == "__main__":
    print(BIENVENIDA)
    ## primero vemos lo de la informacion principal antes de que comiences a usar una terminal
    print('obteniendo tus direcciones ip')
    print(Fore.YELLOW+'Buscando..')
    driver = definir_driver()
    ip_privada = comando('ip add | egrep -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/24"')
    salida_datos(buscar_ip_publica(driver), ip_privada)
    driver.quit()
    



