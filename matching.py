from engine import respone 
from voice_process import VoiceProcess
from json import load
from utils import dataset
from wikipedia import summary
from actions import Actions
def Matching():
  try:
    while True:
      input_text = VoiceProcess() # open the mic and get the voice text
      print("Waiting command...")
      
      if input_text is not None: # check if the mic detect any text
        print('Matching...')

        understand = False
        with open('dataset.json') as file: # read dataset
          data = load(file) # load the json file
          for key in data: # loop in all data keys 
            keys, randomResponse, responses, action = dataset(key)
            if not keys: continue # check if the command have keys or not, if yes skip to sacond loop
            for keyword in keys: # loop inside all keys
              keyword = keyword.lower()
              if keyword in input_text: # check if the input text from mic matches with any key
                understand = True # means that the command is exist in the dataset 
                print(action)
                if action:
                  print('yup')
                  getattr(Actions, action)
                if responses:
                  respone(randomResponse) # output the choosing response as a sound
                # Extra Response
                if key == 'your_name':
                  respone_test = VoiceProcess()
                  _, randomResponse, _, _ = dataset('honor')
                  if respone_test is not None:
                    return respone(randomResponse)
                if key == 'wikipedia':
                  try:
                    query = input_text
                    for filter in keys:
                      query = input_text.replace(filter, "")
                    data = summary(query, sentences=1)
                    if data: return respone(data)
                    else:
                      _, randomResponse, _, _ = dataset('unavailable')
                      respone(randomResponse)
                  except:
                    _, randomResponse, _, _ = dataset('RequestError')
                    respone(randomResponse)
                    
                return
              
        
        if not understand:
          _, randomResponse, _ = dataset('no_sound')
          return respone(randomResponse)
      else:
        return
  except:
    return