from engine import respone 
from voice_process import VoiceProcess
from json import load
from utils import dataset
from wikipedia import summary

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
            keys, responses = dataset(key)
            if not keys: continue # check if the command have keys or not if yes skip this key
            for keyword in keys: # loop inside all keys
              keyword = keyword.lower()
              if keyword in input_text: # check if the input text from mic matches with any key
                understand = True # means that the command is exist in the dataset 
                if responses:
                  output = responses # get random response from key response
                  respone(output) # output the chosin test as a sound
                
                # Extra Response
                if key == 'your_name':
                  respone_test = VoiceProcess()
                  _, responses = dataset('honor')
                  if respone_test is not None:
                    return respone(responses)
                if key == 'wikipedia':
                  try:
                    query = input_text
                    for filter in keys:
                      query = input_text.replace(filter, "")
                    data = summary(query, sentences=1)
                    if data: return respone(data)
                    else:
                      _, responses = dataset('unavailable')
                      respone(responses)
                  except:
                    _, responses = dataset('RequestError')
                    respone(responses)
                    
                return
              
        
        if not understand:
          _, responses = dataset('no_sound')
          return respone(responses)
      else:
        return
  except:
    return