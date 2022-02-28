from json import load
from random import choice
# get response and keys from dataset
def dataset(key):
  """
  returns `keys`, `randomResponse`, `responses`
  """
  with open('dataset.json') as file:
    data = load(file)
    keys = data[key]['keys']
    responses = data[key]['responses']
    action = data[key]['action']
    randomResponse = choice(responses)
    return keys, randomResponse, responses, action
  
# matchs open key
def isWake(text):
  if not text: return False
  isword = 0
  keys, _, _, _ = dataset('wake')
  for keyword in keys:
    if keyword in text:
      isword = 1
      return True
  if not isword: return False
  
  
def getJoke():
  with open('models/jokes.json') as file:
    data = load(file)
    return choice(data)