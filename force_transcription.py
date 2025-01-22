import whisper
import sounddevice as sd
import numpy as np

# Load the Whisper model
model = whisper.load_model("large")  # Use "base", "medium", or "large" as needed

def transcribe_audio(audio_data):
    """
    Function to transcribe audio with a specific language.
    """
    try:
        result = model.transcribe(audio_data, language="en")  # Force transcription in English
        print("Transcription:", result["text"])
    except Exception as e:
        print("Error in transcription:", e)

# Real-time audio input callback
def audio_callback(indata, frames, time, status):
    if status:
        print(f"Status: {status}")
    audio = np.frombuffer(indata, dtype=np.float32)
    transcribe_audio(audio)

# Start recording with the specified sample rate
try:
    print("Listening for audio in English...")
    with sd.InputStream(callback=audio_callback, samplerate=16000, channels=1, dtype="float32"):
        input("Press Enter to stop...\n")  # Keep the stream open until interrupted
except Exception as e:
    print(f"Error: {e}")
