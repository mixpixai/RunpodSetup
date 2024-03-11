#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#@title Environment Setup

from pathlib import Path

OPTIONS = {}

UPDATE_COMFY_UI = True  #@param {type:"boolean"}
WORKSPACE = 'ComfyUI'
OPTIONS['UPDATE_COMFY_UI'] = UPDATE_COMFY_UI

get_ipython().system('[ ! -d $WORKSPACE ] && echo -= Initial setup ComfyUI =- && git clone https://github.com/comfyanonymous/ComfyUI')
get_ipython().run_line_magic('cd', '$WORKSPACE')

if OPTIONS['UPDATE_COMFY_UI']:
  get_ipython().system('echo -= Updating ComfyUI =-')
  get_ipython().system('git pull')

get_ipython().system('echo -= Install dependencies =-')
get_ipython().system('pip install xformers!=0.0.18 -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu121 --extra-index-url https://download.pytorch.org/whl/cu118 --extra-index-url https://download.pytorch.org/whl/cu117')


# # Adding custom Nodes

# In[ ]:


get_ipython().run_line_magic('cd', 'custom_nodes/')


# In[ ]:


get_ipython().system('git clone https://github.com/Gourieff/comfyui-reactor-node.git')
get_ipython().run_line_magic('cd', 'comfyui-reactor-node')
get_ipython().system('python install.py')
get_ipython().run_line_magic('cd', '..')
get_ipython().system('git clone https://github.com/ealkanat/comfyui_easy_padding.git')
get_ipython().system('git clone https://github.com/ssitu/ComfyUI_UltimateSDUpscale --recursive')
get_ipython().system('git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus.git')
get_ipython().system('git clone https://github.com/ltdrdata/ComfyUI-Impact-Pack.git')
get_ipython().system('git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git')
get_ipython().system('git clone https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git')
get_ipython().system('git clone https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git')
get_ipython().system('git clone https://github.com/TinyTerra/ComfyUI_tinyterraNodes.git')
get_ipython().system('git clone https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes.git')
get_ipython().system('git clone https://github.com/cubiq/ComfyUI_essentials.git')

get_ipython().system('git clone https://github.com/Fannovel16/comfyui_controlnet_aux.git')
get_ipython().run_line_magic('cd', 'comfyui_controlnet_aux')
get_ipython().system('pip install -r requirements.txt;')
get_ipython().run_line_magic('cd', '..')

get_ipython().system('git clone https://github.com/FizzleDorf/ComfyUI_FizzNodes.git')
get_ipython().run_line_magic('cd', 'ComfyUI_FizzNodes')
get_ipython().system('pip install -r requirements.txt')
get_ipython().run_line_magic('cd', '..')

get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('ls', '')


# Download some models/checkpoints/vae or custom comfyui nodes (uncomment the commands for the ones you want)

# In[ ]:


# Checkpoints

get_ipython().system('wget -c https://huggingface.co/misri/realismEngineSDXL_v20VAE/resolve/main/realismEngineSDXL_v20VAE.safetensors -P ./models/checkpoints/')
get_ipython().system('wget -c https://huggingface.co/kevin36524/epicrealism_naturalSinRC1VAE/resolve/main/epicrealism_naturalSinRC1VAE.safetensors -P ./models/checkpoints/')
get_ipython().system('wget -c https://huggingface.co/kevin36524/epicrealism_naturalSinRC1VAE/resolve/main/realisticVisionV60B1_v60B1VAE.safetensors -P ./models/checkpoints/')

get_ipython().system('wget -c https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v3_sd15_mm.ckpt -P ./custom_nodes/ComfyUI-AnimateDiff-Evolved/models/')

# VAE
get_ipython().system('wget -c https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors -P ./models/vae/')

# Loras
get_ipython().system('wget -c https://huggingface.co/kevin36524/epicrealism_naturalSinRC1VAE/resolve/main/epiCRealismHelper.safetensors -P ./models/loras')

# T2I-Adapter

# ControlNet
get_ipython().system('wget -c https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_openpose_sd14v1.pth -P ./models/controlnet/')
get_ipython().system('wget -c https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models/t2iadapter_canny_sd14v1.pth -P ./models/controlnet/')
get_ipython().system('wget -c https://huggingface.co/kevin36524/epicrealism_naturalSinRC1VAE/resolve/main/control_v11p_sd15_openpose.pth -P ./models/controlnet/')

# IP Adapter
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-full-face_sd15.safetensors -P ./models/ipadapter/')
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-plus-face_sd15.safetensors -P ./models/ipadapter/')
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-plus_sd15.safetensors -P ./models/ipadapter/')
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-full-face_sd15.bin -P ./models/ipadapter/')
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-plus-face_sd15.bin -P ./models/ipadapter/')
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-plus_sd15.bin -P ./models/ipadapter/')

get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plus_sd15.bin -P ./models/ipadapter/')
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plusv2_sd15.bin -P ./models/ipadapter/')
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plus_sd15_lora.safetensors -P ./models/loras/')
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plusv2_sd15_lora.safetensors -P ./models/loras/')

# CLIPVision model (needed for styles model)
get_ipython().system('wget -c https://huggingface.co/openai/clip-vit-large-patch14/resolve/main/pytorch_model.bin -O ./models/clip_vision/clip_vit14.bin')
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter/resolve/main/models/image_encoder/model.safetensors -O ./models/clip_vision/CLIP-ViT-H-14-laion2B-s32B-b79K-model.safetensors')
get_ipython().system('wget -c https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/image_encoder/model.safetensors -O ./models/clip_vision/CLIP-ViT-bigG-14-laion2B-39B-b160k-model.safetensors')

# ESRGAN upscale model
get_ipython().system('wget -c https://huggingface.co/FacehugmanIII/4x_foolhardy_Remacri/resolve/main/4x_foolhardy_Remacri.pth -P ./models/upscale_models')

# Facestore models
get_ipython().system('wget -c https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth -P ./models/facerestore_models')

get_ipython().system('wget -c https://huggingface.co/latent-consistency/lcm-lora-sdv1-5/resolve/main/pytorch_lora_weights.safetensors -O ./models/loras/lcm-lora-sdv1-5_pytorch_lora_weights.safetensors')

