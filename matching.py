from engine import response 
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
            keys, random_response, responses, action = dataset(key)
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
                  response(random_response) # output the choosing response as a sound
                # Extra Response
                if key == 'your_name':
                  response_test = VoiceProcess()
                  _, random_response, _, _ = dataset('honor')
                  if response_test is not None:
                    return response(random_response)
                if key == 'wikipedia':
                  try:
                    query = input_text
                    for filter in keys:
                      query = input_text.replace(filter, "")
                    data = summary(query, sentences=1)
                    if data: return response(data)
                    else:
                      _, random_response, _, _ = dataset('unavailable')
                      response(random_response)
                  except:
                    _, random_response, _, _ = dataset('RequestError')
                    response(random_response)
                    
                return
              
        
        if not understand:
          _, random_response, _ = dataset('no_sound')
          return response(random_response)
      else:
        return
  except:
    return