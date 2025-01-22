import sounddevice as sd

def callback(indata, frames, time, status):
    print("Audio input recieved:", indata)

with sd.InputStream(callback=callback):
     print("Listening...")
     sd.sleep(10000)
