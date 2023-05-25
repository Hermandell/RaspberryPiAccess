# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import base64
import requests
import drivers

# Configuracion de los pines de la Raspberry Pi
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Inicializacion del lector RFID
reader = SimpleMFRC522()
#LCD i2C
display = drivers.Lcd()

# Ciclo infinito para leer las tarjetas RFID
while True:

    # Espera a que se coloque una tarjeta en el lector
    display.lcd_display_string("Acerque la tarjeta..",4)
    id, text = reader.read()
    #print(text)
    # Decodificacion del texto en base64
    decoded_text = base64.b64decode(text)
    #print(type(decoded_text))
    data_str = decoded_text.decode('utf-8')
    # Verificacion de la presencia del simbolo '&'
    if '&' not in data_str:
        display.lcd_clear()
        display.lcd_display_string("Acceso denegado",2)
        continue
    data_str = data_str.strip().replace(' ', '').replace('b', '')
    ncontrol, password = data_str.split('&')
    payload = {
    'ncontrol': ncontrol,
    'password': password
    }
    #print(payload)
    # Realización del request
    response = requests.post('https://flaskapi-mu.vercel.app/all', json=payload)

    # Verificación del status code del request
    if response.status_code == 200:
        objeto = response.json()[0]
        nombre = str(objeto['nombre'])
        objeto2= response.json()[1]
        estatus = str(objeto2['estatus'])
        #print(nombre)
        #print("Acceso correcto")
        display.lcd_clear()
        display.lcd_display_string("Acceso correcto", 1)
        display.lcd_display_string(nombre, 2)
        display.lcd_display_string(estatus, 3)

    else:
        display.lcd_clear()
        display.lcd_display_string("Acceso Denegado", 1)
    
    GPIO.cleanup()
