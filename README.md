## Description

This project demonstrates how to set up and test OpenAI's Whisper model for real-time speech-to-text transcription on Ubuntu 24.04.1 LTS. It includes instructions for installing dependencies, configuring the environment, and running a real-time transcription script using Python.


## Features

- Real-time speech-to-text transcription using OpenAI Whisper.
- Support for different Whisper models (`tiny`, `base`, `small`, `medium`, `large`).
- Handles real-time audio capture via the `sounddevice` library.
- Adjustable audio parameters like sample rate and chunk duration.
  
## Prerequisites

- Ubuntu 24.04.1 LTS
- Python 3.8 or higher
- Compatible GPU with CUDA support (optional, for faster processing)
- A working microphone

##Installation
Provide a step-by-step guide to set up the project:

1.Create and Activate a Virtual Environment -

python3 -m venv venv
source venv/bin/activate

2.Install Dependencies -

pip install --upgrade pip
pip install openai-whisper sounddevice numpy ffmpeg-python

3.Install CUDA (Optional, for GPU Support)-

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117

4.Running the Project -

## Running the Project

1. **Activate the virtual environment**:
  
   source venv/bin/activate

   python3 real_time_transcription.py

 Troubleshooting
 
Microphone Not Detected: Run the following to list all available devices:

python3 -m sounddevice

Then set the correct device ID in the script

sd.default.device = <device_id>


Acknowledge tools or libraries used:
## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper)
- [SoundDevice](https://python-sounddevice.readthedocs.io/)
- [PyTorch](https://pytorch.org/)



