from machine import Pin
import time

# Configuración de pines
tilt_pin = Pin(14, Pin.IN)  # Pin de señal del sensor Tilt switch
buzzer_pin = Pin(21, Pin.OUT)

try:
    while True:
        # Leer el estado del sensor Tilt switch
        tilt_state = tilt_pin.value()

        # Si el sensor Tilt switch está activado, encender el zumbador
        if tilt_state == 1:
            buzzer_pin.on()
            print("¡Tilt switch activado! Buzzer encendido.")
        else:
            buzzer_pin.off()
            print("Tilt switch desactivado. Buzzer apagado.")

        time.sleep(0.1)  # Esperar un breve período antes de la siguiente lectura

except KeyboardInterrupt:
    print("Programa interrumpido")