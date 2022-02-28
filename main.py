from matching import Matching
from engine import respone
from voice_process import VoiceProcess
from utils import isWake, dataset

# cases = {
#   'talking': "assets/talking.gif",
#   'sleeping': 'assets/sleeping.gif',
#   'waiting': 'assets/waiting.gif'
# }

def run():
  print('Waiting Key..')
  once = False
  key = VoiceProcess()
  keyIsMatch = isWake(key)
  
  while keyIsMatch:
    try:
      print('I\'m Listening..')
      if not once:
        _, randomResponse, _, _ = dataset('wake')
        respone(randomResponse)
      Matching()
      once = True
    except:
      break
  if not keyIsMatch: run()
  
  
run()
