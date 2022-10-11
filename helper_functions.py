import pyaudio 
from vosk import Model, KaldiRecognizer
import json
# importing model, vosk was used because it s free of charge any text to speech library can be used instead
model = Model(model_name="vosk-model-en-us-0.22")


# Defining the record microphone function
CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

def record_microphone(messages, index, recordings, chunk=1024):
    p = pyaudio.PyAudio()

    stream = p.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=FRAME_RATE,
                    input=True,
                    input_device_index=index,
                    frames_per_buffer=chunk)

    frames = []
    # Check if the queue messages is empty and if not keep recording
    while not messages.empty():
        # print("recording working")
        data = stream.read(chunk)
        frames.append(data)
        if len(frames) >= (FRAME_RATE * RECORD_SECONDS) / chunk:
            recordings.put(frames.copy())
            frames = []

    stream.stop_stream()
    stream.close()
    p.terminate()

rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)

def speech_recognition(messages, recordings, output):
    # Check if the queue messages is empty and if not keep transcribing
    while not messages.empty():
        frames = recordings.get()
        rec.AcceptWaveform(b''.join(frames))
        result = rec.Result()
        text = json.loads(result)["text"]
        print("Transcribe function working")
        # Put the text into the queue output which will be unloaded in the app.py 
        output.put(text)