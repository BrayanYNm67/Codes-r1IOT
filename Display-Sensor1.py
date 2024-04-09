from machine import Pin, I2C
import ssd1306
import time

# Configuración del sensor KY020 (sensor de movimiento)
pir_pin = Pin(14, Pin.IN)  # Conectado al pin GPIO14
# Configuración del display OLED
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Configura I2C en los pines GPIO21 (SDA) y GPIO22 (SCL)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # Crear un objeto SSD1306 OLED

# Mensaje a mostrar cuando se detecta movimiento
mensaje_movimiento = "¡Movimiento detectado!"

while True:
    if pir_pin.value() == 1:  # Si se detecta movimiento
        oled.fill(0)  # Limpiar la pantalla
        oled.text(mensaje_movimiento, 0, 0)  # Mostrar mensaje de movimiento
        oled.show()  # Actualizar la pantalla OLED
    else:
        oled.fill(0)  # Limpiar la pantalla si no hay movimiento
        oled.show()  # Actualizar la pantalla OLED
    time.sleep(0.1)  # Esperar un corto periodo antes de volver a verificar el sensor de movimiento