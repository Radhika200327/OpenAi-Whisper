import whisper
import sounddevice as sd
import numpy as np
import wave

# Load the Whisper model
model = whisper.load_model("base")  # Change to "small", "medium", "large" for more accuracy

# Set audio recording parameters
SAMPLE_RATE = 16000  # Required by Whisper
DURATION = 20  # Recording duration in seconds per chunk

print("Whisper Real-Time Transcription\nPress Ctrl+C to stop.\n")

def record_and_transcribe():
    try:
        while True:
            print("Listening for the next chunk...")

            # Record audio
            audio_data = sd.rec(
                int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype="float32"
            )
            sd.wait()  # Wait for the recording to complete

            # Save the recorded audio to a .wav file for debugging
            with wave.open('debug_audio.wav', 'wb') as wf:
                wf.setnchannels(1)  # Mono channel
                wf.setsampwidth(2)  # 2 bytes per sample (16-bit audio)
                wf.setframerate(SAMPLE_RATE)
                wf.writeframes((audio_data * 32767).astype(np.int16).tobytes())

            # Convert audio to the format expected by Whisper
            audio_data = np.squeeze(audio_data)

            # Transcribe the audio
            print("Transcribing...")
            result = model.transcribe(audio_data, fp16=False)  # Set fp16=False if running on CPU
            print("Transcription:", result["text"])
    except KeyboardInterrupt:
        print("\nTranscription stopped.")

# Ensure the sounddevice module is properly initialized
try:
    sd.check_input_settings(device=None, channels=1)
    record_and_transcribe()
except Exception as e:
    print("Error:", e)
    print("Check your microphone connection and try again.")
