import sqlite3
from datetime import datetime
import random
import time

db_path = "/home/pi/lora_logs/lora_combined.db"

def log_lora_packet():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    for i in range(3):
        now = datetime.utcnow().isoformat()
        freq = round(random.uniform(865.0, 867.0), 3)
        sf = f"SF{random.choice([7, 8, 9, 10, 11, 12])}"
        rssi = random.randint(-120, -90)
        snr = round(random.uniform(5.0, 12.0), 2)
        payload = f"SamplePayload{i}"
        cur.execute("INSERT INTO lora_packets VALUES (?, ?, ?, ?, ?, ?)",
                    (now, freq, sf, rssi, snr, payload))
        print(f"📡 Logged LoRa packet {i+1}")
        time.sleep(1)
    conn.commit()
    conn.close()

def simulate_rf_scan():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    now = datetime.utcnow().isoformat()
    freq_range = "864-868 MHz"
    max_power = round(random.uniform(-60.0, -30.0), 2)
    cur.execute("INSERT INTO rf_scans VALUES (?, ?, ?)", (now, freq_range, max_power))
    print(f"📶 RF Scan logged: {freq_range} | Max Power: {max_power} dBm")
    conn.commit()
    conn.close()

log_lora_packet()
simulate_rf_scan()
