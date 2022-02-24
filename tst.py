# from vosk import Model, KaldiRecognizer
# from pyaudio import PyAudio, paInt16


# model = Model('models/ar')
# recognizer = KaldiRecognizer(model, 16000)


# cap = PyAudio()
# stream = cap.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
# stream.start_stream()

# while True: 
#   data = stream.read(4096)
#   if recognizer.AcceptWaveform(data):
#     print(f"Result: {recognizer.Result()}")

import json

f = open('dataset.json')
data = json.load(f)

for key in data:
  for keyword in data[key]['keys']:
    print(keyword)
