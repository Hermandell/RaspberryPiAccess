import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import base64

reader = SimpleMFRC522()

try:
    # Solicita al usuario el texto a codificar
    text = input('Introduce el texto a codificar: ')
    
    # Codifica el texto en Base64
    encoded_text = base64.b64encode(text.encode('utf-8'))
    
    # Escribe el texto codificado en la tarjeta RFID
    print("Pon tu tarjeta en el lector")
    reader.write(encoded_text.decode('utf-8'))
    print("Texto codificado guardado en la tarjeta RFID")
    
    # Lee el texto de la tarjeta RFID y lo decodifica
    print("Ahora lee la tarjeta RFID para decodificar el texto")
    id, encoded_text = reader.read()
    decoded_text = base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
    print(f"Texto decodificado: {decoded_text}")
    
finally:
    GPIO.cleanup()
