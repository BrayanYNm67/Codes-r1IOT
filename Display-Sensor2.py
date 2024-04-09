from machine import Pin, I2C
import ssd1306
import time

# Configuration of the KY020 motion sensor
pir_pin = Pin(14, Pin.IN)  # Connected to GPIO14 pin
# Configuration of the OLED display
i2c = I2C(0, scl=Pin(26), sda=Pin(25))  # Configure I2C on GPIO21 (SDA) and GPIO22 (SCL) pins
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # Create an SSD1306 OLED object

# Message to display when motion is detected
mensaje_movimiento = "En movimiento"

while True:
    if pir_pin.value() == 1:  # If motion is detected
        print("¡Movimiento detectado!")  # Print message to console
        oled.fill(0)  # Clear the screen
        oled.text(mensaje_movimiento, 0, 0)  # Show motion message
        oled.show()  # Update the OLED display
    else:
        print("No se detecta movimiento")  # Print message to console if no motion is detected
        oled.fill(0)  # Clear the screen if no motion is detected
        oled.show()  # Update the OLED display
    time.sleep(0.1)  # Wait a short period before checking the motion sensor again