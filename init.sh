#!/bin/bash
apt update
apt install -y psmisc ffmpeg vim
source venv/bin/activate
cd /workspace/ComfyUI
python main.py --listen 0.0.0.0 
