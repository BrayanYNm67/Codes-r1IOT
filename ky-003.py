from machine import Pin
import time

# Configuración del pin del sensor KY-003 (reemplaza KY003_SENSOR_PIN)
KY003_SENSOR_PIN = 35  # Ajusta este número según el pin que estés usando

# Configuración del pin del buzzer
BUZZER_PIN = 19  # Ajusta este número según el pin que estés usando
buzzer = Pin(BUZZER_PIN, Pin.OUT)

# Configurar el sensor KY-003
ky003_sensor = Pin(KY003_SENSOR_PIN, Pin.IN)

# Bucle principal
while True:
    if ky003_sensor.value():  # Si el sensor KY-003 detecta una señal (puede ser luz, presión, etc.)
        print("Se detectó una señal")
        buzzer.on()  # Enciende el buzzer
        time.sleep(1)  # Espera un segundo
        buzzer.off()  # Apaga el buzzer
