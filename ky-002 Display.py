from machine import Pin, ADC, I2C
import ssd1306
import time

# Configuración del sensor de choque (KY-002)
pin_sensor_shock = Pin(4, Pin.IN)  # Cambia el número del pin según tu configuración
adc = ADC(pin_sensor_shock)

# Configuración del display OLED (128x64)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Cambia los pines SCL y SDA según tu configuración
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Función para leer el sensor de choque
def leer_sensor_shock():
    return adc.read()

# Función para actualizar el display OLED con el valor del sensor de choque
def actualizar_display(valor):
    oled.fill(0)  # Borra el display
    oled.text("Sensor de Choque", 0, 0)
    oled.text("Valor:", 0, 20)
    oled.text(str(valor), 60, 20)
    oled.show()  # Muestra en pantalla

# Bucle principal
while True:
    valor_sensor = leer_sensor_shock()
    actualizar_display(valor_sensor)
    time.sleep(0.1)  # Espera un breve tiempo antes de volver a leer el sensor
