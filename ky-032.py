import ssd1306
from machine import Pin, I2C
import time

# Configuración del sensor de evitación de obstáculos
obstacle_sensor_pin = 14
obstacle_sensor = Pin(obstacle_sensor_pin, Pin.IN)

# Configuración del display OLED
i2c = I2C(scl=Pin(26), sda=Pin(25))  # Asigna los pines SCL y SDA para la comunicación I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Textos a mostrar en el display uno por uno cuando se detecte un obstáculo
texts = ["Nombre: Brayan", "Edad: 19", "Telefono: 4181848054", "Calle: Main", "Grupo: GDS0552"]

while True:
    if obstacle_sensor.value() == 0:  # Si se detecta un obstáculo
        for text in texts:
            oled.fill(0)  # Limpia la pantalla
            oled.text(text, 0, 0)  # Imprime el mensaje en el display OLED
            oled.show()  # Actualiza la pantalla con el mensaje
            time.sleep(1)  # Espera un segundo antes de mostrar el siguiente mensaje
    else:
        oled.fill(0)  # Limpia la pantalla cuando no se detecta un obstáculo
        oled.show()  # Actualiza la pantalla para borrar cualquier mensaje anterior
    time.sleep(0.1)  # Espera un corto período antes de volver a verificar el sensor de evitación de obstáculos
