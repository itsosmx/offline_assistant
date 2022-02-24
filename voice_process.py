from vosk import Model, KaldiRecognizer
from pyaudio import PyAudio, paInt16


model = Model('models/en')
recognizer = KaldiRecognizer(model, 16000)

def VoiceProcess(): 
  try:
    initialize = PyAudio()
    stream = initialize.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True: 
      data = stream.read(4096)
      if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        text = text.lower()
        print(f'input: {text}')
        return text
  except:
    print('RecognizeVoice Error')