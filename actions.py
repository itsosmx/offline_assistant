from datetime import datetime
from utils import getJoke
from engine import respone

class Actions:
  # def __init__(self, action_name):
  #   self.action_name = action_name
  date = datetime.now()
  
  def get_date(self):
    Date = self.date.strftime("%x")
    return respone(f'Date is {Date}')
  def get_today(self):
    Date = self.date.strftime("%A")
    return respone(f'Today is {Date}')
  def get_time(self):
    Date = self.date.strftime("%I:%M %p")
    respone(f'The time is {Date}')
  def get_joke(self):
    respone(getJoke())