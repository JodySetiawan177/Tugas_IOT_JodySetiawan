import paho.mqtt.client as mqtt
import json, time, random
from datetime import datetime

BROKER = "localhost"
TOPIC_SENSOR = "iot/sensor"
TOPIC_KONTROL = "iot/kontrol"

# Fungsi saat berhasil terhubung ke Mosquitto
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Terhubung ke Broker MQTT (Code: {reason_code})")
    client.subscribe(TOPIC_KONTROL) # Mendengarkan perintah kontrol lampu

# Fungsi saat menerima perintah dari Node-RED
def on_message(client, userdata, msg):
    print(f"\n[AKTUATOR] Perintah diterima: {msg.payload.decode()}\n")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="ESP32-Simulator")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_start()

print("ESP32 Simulator berjalan... Tekan Ctrl+C untuk berhenti")
try:
    while True:
        # Membuat data suhu acak antara 25.0 - 34.0 °C
        data = {
            "suhu": round(random.uniform(25.0, 34.0), 1),
            "kelembaban": round(random.uniform(55.0, 80.0), 1),
            "timestamp": datetime.now().isoformat()
        }
        client.publish(TOPIC_SENSOR, json.dumps(data))
        print(f"-> Kirim data: {data}")
        time.sleep(3)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()