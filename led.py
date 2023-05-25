import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) ## GPIO 18 como salida

def blink():
        print("Ejecución de la función blink...")
        for iteracion in range(10): ## Segundos que durara la funcion
                GPIO.output(18, True) ## Enciendo el 18
                time.sleep(0.5) ## Esperamos 0.5 segundo
                GPIO.output(18, False) ## Apago el 18
                time.sleep(0.5) ## Esperamos 0.5 segundo
                print(iteracion)
        print("Ejecucion de la función blink finalizada")
        GPIO.cleanup() ## Hago una limpieza de los GPIO

# Código principal desde el que usamos todas las funciones
blink()
