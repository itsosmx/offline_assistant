from datetime import datetime
from utils import getJoke
from engine import response

class Actions:
  # def __init__(self, action_name):
  #   self.action_name = action_name
  date = datetime.now()
  
  def get_date(self):
    Date = self.date.strftime("%x")
    return response(f'Date is {Date}')
  def get_today(self):
    Date = self.date.strftime("%A")
    return response(f'Today is {Date}')
  def get_time(self):
    Date = self.date.strftime("%I:%M %p")
    response(f'The time is {Date}')
  def get_joke(self):
    response(getJoke())