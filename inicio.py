import ip_publica as publica
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
    ip_privada = comando('ip add | egrep -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/24"')
    salida_datos(publica.obtener_ip_publica(), ip_privada)    



