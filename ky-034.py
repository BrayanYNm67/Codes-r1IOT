from machine import TouchPad, Pin
from umqtt.simple import MQTTClient
import time

# Configuración del sensor táctil
touch_pin = TouchPad(Pin(4))

# Configuración del LED bicolor
led_pin_out = Pin(2, Pin.OUT)

# Configuración de la red Wi-Fi
ssid = "No Paso Internet Ivana"
password = "123456789"
mqtt_broker = "192.168.68.200"  # Cambiar a la dirección IP de tu broker MQTT
mqtt_topic = "utng/arg/flash"

# Función para conectar a Wi-Fi
def connect_wifi():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectando a WiFi...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("Conexión WiFi exitosa")

# Función para conectar a MQTT
def connect_mqtt():
    client = MQTTClient("esp32", mqtt_broker)
    client.connect()
    print("Conexión MQTT exitosa")
    return client

# Función para leer el valor del sensor táctil
def leer_sensor():
    try:
        valor = touch_pin.read()
        return valor < 300
    except Exception as e:
        return False

# Función para publicar un mensaje MQTT cuando se toca el sensor
def publish_touch_event(client):
    client.publish(mqtt_topic, b"Tocado")
    print("Mensaje MQTT publicado: Tocado")

# Función principal
def main():
    connect_wifi()
    mqtt_client = connect_mqtt()

    while True:
        tocado = leer_sensor()
        if tocado:
            led_pin_out.on()  # Enciende el LED flash cuando se toca el sensor
            publish_touch_event(mqtt_client)
        else:
            led_pin_out.off()
        time.sleep(1)  # Espera antes de volver a leer el sensor

if __name__ == "__main__":
    main()