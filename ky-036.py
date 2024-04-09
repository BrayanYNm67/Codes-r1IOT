from machine import Pin, TouchPad
import time

# Configura el pin del sensor táctil
pin_touch = Pin(4)  # Cambia el número del pin según tu configuración
touch = TouchPad(pin_touch)

# Función para leer el estado del sensor táctil
def leer_sensor():
    return touch.read()

# Bucle principal
while True:
    valor = leer_sensor()
    if valor < 400:  # Ajusta este umbral según las características de tu sensor
        print("¡Se detectó un toque!")
    time.sleep(0.1)  # Espera un breve tiempo antes de volver a leer el sensor
