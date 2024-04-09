from machine import Pin
import time

# Configura los pines del sensor de rastreo KY-033
pin_sensor1 = Pin(4, Pin.IN)  # Pin izquierdo del sensor
pin_sensor2 = Pin(5, Pin.IN)  # Pin derecho del sensor

# Función para leer el estado de los sensores
def leer_sensores():
    return pin_sensor1.value(), pin_sensor2.value()

# Bucle principal
while True:
    valor_sensor1, valor_sensor2 = leer_sensores()
    if valor_sensor1 == 0 or valor_sensor2 == 0:  # Si alguno de los sensores detecta una línea
        print("¡Se detectó una línea!")
    time.sleep(0.1)  # Espera un breve tiempo antes de volver a leer los sensores
