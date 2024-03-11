#!/bin/bash
apt update
apt install -y vim
cd /workspace/ComfyUI
python main.py --listen 0.0.0.0 
