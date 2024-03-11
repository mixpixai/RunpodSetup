#!/bin/bash
apt update

# by default the network volume is mounted to /runpod-volume in serverless, while /workspace in regular pods
export RUNPOD_NETWORK_VOLUME_PATH="/workspace"

if [ -n "$RUNPOD_ENDPOINT_ID" ]; then
    export RUNPOD_NETWORK_VOLUME_PATH="/runpod-volume"
fi

export COMFY_OUTPUT_PATH=$RUNPOD_NETWORK_VOLUME_PATH/ComfyUI/output
export PATH="$RUNPOD_NETWORK_VOLUME_PATH/venv/bin:$PATH"

cd $RUNPOD_NETWORK_VOLUME_PATH

ls
pwd

# Use libtcmalloc for better memory management
TCMALLOC="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"
export LD_PRELOAD="${TCMALLOC}"

echo "runpod-worker-comfy: Starting ComfyUI"
#python $RUNPOD_NETWORK_VOLUME_PATH/ComfyUI/main.py --disable-auto-launch --disable-metadata &
python $RUNPOD_NETWORK_VOLUME_PATH/ComfyUI/main.py --disable-metadata &

sleep 15;

echo "runpod-worker-comfy: Starting RunPod Handler"
python -u $RUNPOD_NETWORK_VOLUME_PATH/rp_handler.py
