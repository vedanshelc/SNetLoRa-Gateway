#!/bin/bash

echo "🔧 Starting Raspberry Pi Setup for LoRa Intercept Gateway..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y git build-essential cmake libtool pkg-config sqlite3 python3-pip

# Create log directory
mkdir -p ~/lora_logs

# Create SQLite database
sqlite3 ~/lora_logs/lora_combined.db "
CREATE TABLE IF NOT EXISTS lora_packets (
    timestamp TEXT,
    frequency REAL,
    spreading_factor TEXT,
    rssi REAL,
    snr REAL,
    payload TEXT
);
CREATE TABLE IF NOT EXISTS rf_scans (
    timestamp TEXT,
    frequency_range TEXT,
    max_power REAL
);
"

# Download global config
curl -o ~/lora_logs/global_conf_IN865.json https://raw.githubusercontent.com/YOUR_USERNAME/SNetLoRa-Gateway/main/global_conf_IN865.json

# Download logger
curl -o ~/lora_logs/lora_combined_logger.py https://raw.githubusercontent.com/YOUR_USERNAME/SNetLoRa-Gateway/main/lora_combined_logger.py

echo "✅ Setup complete. To start logging:"
echo "python3 ~/lora_logs/lora_combined_logger.py"
