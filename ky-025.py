from machine import Pin
import time

# Configuración de los pines del módulo ULN2003A para el motor paso a paso 28BYJ-48
IN1_PIN_MOTOR1 = 27
IN2_PIN_MOTOR1 = 26
IN3_PIN_MOTOR1 = 14
IN4_PIN_MOTOR1 = 12

IN1_PIN_MOTOR2 = 25
IN2_PIN_MOTOR2 = 33
IN3_PIN_MOTOR2 = 15
IN4_PIN_MOTOR2 = 13

# Configuración del pin del sensor KY-025 (reemplaza SOUND_SENSOR_PIN)
KY025_SENSOR_PIN = 35  # Ajusta este número según el pin que estés usando

# Configurar pines del motor paso a paso
motor1_pins = [Pin(pin, Pin.OUT) for pin in [IN1_PIN_MOTOR1, IN2_PIN_MOTOR1, IN3_PIN_MOTOR1, IN4_PIN_MOTOR1]]
motor2_pins = [Pin(pin, Pin.OUT) for pin in [IN1_PIN_MOTOR2, IN2_PIN_MOTOR2, IN3_PIN_MOTOR2, IN4_PIN_MOTOR2]]

# Patrones de secuencia de pasos para el motor paso a paso
motor_seq = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# Configurar el sensor KY-025
ky025_sensor = Pin(KY025_SENSOR_PIN, Pin.IN)

# Función para activar los motores
def activate_motors():
    for _ in range(512):  # Cambia este valor según la cantidad de pasos que desees dar
        for step in motor_seq:
            for i, pin in enumerate(motor1_pins):
                pin.value(step[i])
            for i, pin in enumerate(motor2_pins):
                pin.value(step[i])
            time.sleep_ms(10)  # Puedes ajustar el retardo aquí para controlar la velocidad de los motores

# Bucle principal
while True:
    if ky025_sensor.value():  # Si el sensor KY-025 detecta una señal
        print("Se detectó una señal")
        activate_motors()  # Activar los motores
