from machine import Pin, ADC
import time

# Configura el pin del sensor de llama
pin_flame = Pin(4, Pin.IN)  # Cambia el número del pin según tu configuración
adc = ADC(pin_flame)

# Función para leer el estado del sensor de llama
def leer_sensor():
    return adc.read()

# Bucle principal
while True:
    valor = leer_sensor()
    if valor < 1000:  # Ajusta este umbral según las características de tu sensor
        print("¡Se detectó una llama!")
    time.sleep(0.1)  # Espera un breve tiempo antes de volver a leer el sensor
