from machine import Pin, PWM
import time

# Configuración de los pines para el LED RGB
pin_red = Pin(12, Pin.OUT)
pin_green = Pin(13, Pin.OUT)
pin_blue = Pin(14, Pin.OUT)

# Inicialización de los pines PWM para controlar la intensidad de cada color
pwm_red = PWM(pin_red)
pwm_green = PWM(pin_green)
pwm_blue = PWM(pin_blue)

# Función para cambiar el color del LED RGB
def cambiar_color(red, green, blue):
    pwm_red.duty(red)
    pwm_green.duty(green)
    pwm_blue.duty(blue)

# Bucle principal
while True:
    # Rojo
    print("Rojo")
    cambiar_color(1023, 0, 0)
    time.sleep(1)
    
    # Verde
    print("Verde")
    cambiar_color(0, 1023, 0)
    time.sleep(1)
    
    # Azul
    print("Azul")
    cambiar_color(0, 0, 1023)
    time.sleep(1)
