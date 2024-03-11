# RunpodSetup
- MixPix AI uses runpod serverless for executing ComfyUI Workflow.

## Basic Setup Overview
- First create a network drive in Runpod using a GPU based VM.
- Then perform the initial setup like intalling ComfyUI, Virtual Env, Hugging face model etc.
- Once that is done you can use serverless functions to mount your network drive to perform on demand workflows.

## 
- References
- [Runpod blog post for Network Drive based serverless](https://blog.runpod.io/runpod-serverless-no-docker-stress/)
- [Worker ComfyUI Docker for reference](https://github.com/blib-la/runpod-worker-comfy/tree/main)

## Detailed Steps (WIP)
- [Step-1] First create a Network drive in Runpod. I am using 100GB network drive.
  - Go to https://www.runpod.io/console/user/storage
  - Tap on `New Network Volume`
  - Choose your Data Center, Name and Size (Note you will not be able to edit the size later. Might want to use somewhere between 75GB to 100GB).
 
- [Step-2] Next go to https://www.runpod.io/console/pods
  - Tap on `+ GPU Pod`
  - Tap on `Select Network Volume` and choose your Network Volume you created in the above step.
  - Tap on one of the available Machines based on your cost affordability.
  - Tap on `Type to search for a template` and choose a template that works for you. I am using `RunPod Pytorch 2.1(runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04
)`
  - Next Customize Deployment, Expose TCP Ports ==> `22, 8188`, Click `Set Overrides`. This will expose port 8188 so that you can use ComfyUI without tunneling.
  - [Optional] Choose Spot(Interruptible) if you want to spend less cost and don't mind interruptions.
  - Hit `Continue`
 
- [Step-3] [Initial first time only] Next Launch the Jupiter Notebook and do the initial setup
  - Open terminal
  - `python -m venv venv`
  - `source venv/bin/activate`
  - `git clone https://github.com/mixpixai/RunpodSetup.git`
  - `mv RunpodSetup/* .`
  - `pip install runpod`
  - `ipython comfyui_colab_v2.py`
 
- [Step-4] [Making your workflow] If you need to make a new workflow or add some models you can follow these steps.
  -  Create your Pod as mentioned in Step-2
  -  Open Jupiter terminal
  -  `source venv/bin/activate`
  -  `./init.sh`
  -  Go to [Pods Dashboard](https://www.runpod.io/console/pods)
  -  Tap on Connect > TCP Port mappings.
  -  Check your public IPAddress and the port-id for 8188 and open it in new tab. Something like `http://69.30.85.113:22139/`
  -  Now create your workflow if needed. Test if the basic prompt is working and generating the image.
  -  To download the workflow as api. Tap on Settings in ComfyUI. Enable Developer mode.
  -  Download `Save (API format)`. This will download it in API format.

- [Step-5] Create your Serverless Template
  - Go to https://www.runpod.io/console/user/templates
  - Tap `New Template`
    - Give some `name`
    - Choose `serverless` in template Type
    - Add your container Image. I am using `runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04`
    - Container Disk  `15 GB`
    - Hit `Save Template`
   
- [Step-6] Create a new serverless endpoint
  - Go to https://www.runpod.io/console/serverless
  - Tap `+ New Endpoint`
    - Give some endpoint name eg: `workflow_api`
    - Choose your preferred GPU workers.
    - Confirm Active workes are 0 and Max workers are 3
    - Enable `Flashbot`
    - Continer Configuration - `Select the template from Step-5`
    - `IMP` - Advanced - Select your network volume.
    - Scale Type - You can choose Queue Delay or Request Count.


