


NAMA : JODY SETIAWAN
NPM : 2410010177

1. **MQTT Ingestion (`iot/sensor` & `iot/kontrol`)**: Komunikasi real-time antara simulator perangkat dengan broker Mosquitto.
2. **REST API & Autentikasi (`X-API-Key`)**:
   - `GET /api/suhu`: Mengambil data sensor terbaru.
   - `GET /api/history`: Mengambil riwayat data sensor dari database SQLite.
   - `POST /api/kontrol`: Mengirim perintah aktuator lampu (`on`/`off`).
   - `PUT /api/threshold`: Mengubah batas suhu peringatan secara dinamis.
3. **WebSocket Real-Time (`/ws/sensor`)**: Pembaruan angka dan grafik **Chart.js** tanpa perlu refresh halaman.
4. **Penyimpanan Database SQLite (`iot_history.db`)**: Pencatatan otomatis seluruh data sensor masuk.

## Struktur Folder
- `simulator/simulasi_esp32.py` — Program simulator sensor & aktuator ESP32.
- `nodered/flows.json` — Konfigurasi flow backend Node-RED & halaman dashboard.
- `web/dashboard.html` — Antarmuka dashboard web.
- `database/iot_history.db` — File database SQLite berisi log sensor.

## Cara Menjalankan
1. Jalankan broker Mosquitto (`port 1883`) dan Node-RED (`node-red`).
2. Import file `nodered/flows.json` ke Node-RED lalu klik **Deploy**.
3. Jalankan simulator: `python simulator/simulasi_esp32.py`.
4. Buka dashboard melalui browser di `http://localhost:1880/dashboard`.