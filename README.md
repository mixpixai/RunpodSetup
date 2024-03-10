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
- First create a Network drive in Runpod. I am using 100GB network drive.
  - Go to https://www.runpod.io/console/user/storage
  - Tap on `New Network Volume`
  - Choose your Data Center, Name and Size (Note you will not be able to edit the size later. Might want to use somewhere between 75GB to 100GB).
 
- Next go to https://www.runpod.io/console/pods
  - Tap on `+ GPU Pod`
  - Tap on `Select Network Volume` and choose your Network Volume you created in the above step.
  - Tap on one of the available Machines based on your cost affordability.
  - Tap on `Type to search for a template` and choose a template that works for you. I am using `RunPod Pytorch 2.1`
  - Next Customize Deployment, Expose TCP Ports ==> `22, 8188`, Click `Set Overrides`. This will expose port 8188 so that you can use ComfyUI without tunneling.
  - [Optional] Choose Spot(Interruptible) if you want to spend less cost and don't mind interruptions.
  - Hit `Continue`
