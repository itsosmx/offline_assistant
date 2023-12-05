import pyttsx3
# import os
init  = pyttsx3.init()
AIvoices = init.getProperty('voices')

# windows voices
voices = {
  'male':  AIvoices[0].id,
  'arabic_male': AIvoices[1].id,
  # 'arabic_female': AIvoices[2].id,
  # 'female': AIvoices[3].id,
}

init.setProperty('voice', voices.get(1))

def response(message):
  init.say(message)
  init.runAndWait()  
  
# def response_ar(message):
#   os.system(f'echo "{message}" | festival --language arabic --tts')