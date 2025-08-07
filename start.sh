#!/bin/bash

# Update and install Chrome
apt-get update && apt-get install -y wget unzip curl
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb || apt --fix-broken install -y

# Start the Flask app with Gunicorn
gunicorn timeless:app