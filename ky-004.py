from machine import Pin
import time

# Configura el pin del botón
pin_boton = Pin(4, Pin.IN, Pin.PULL_UP)  # Cambia el número del pin según tu configuración

# Función para leer el estado del botón
def leer_boton():
    return pin_boton.value()

# Bucle principal
while True:
    estado = leer_boton()
    if estado == 0:  # 0 cuando se presiona el botón (debido al pull-up)
        print("¡El botón fue presionado!")
        while leer_boton() == 0:
            time.sleep(0.1)  # Espera a que el botón sea liberado
    time.sleep(0.1)  # Espera un breve tiempo antes de volver a leer el botón
