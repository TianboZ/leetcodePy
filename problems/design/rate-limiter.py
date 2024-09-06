from collections import deque

class Logger:
  def __init__(self):
    self.map = {} # <message: last t>

  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    if message not in self.map:
      self.map[message] = timestamp
      return True
    
    prevT = self.map[message]
    if prevT <= timestamp - 10:
      self.map[message] = timestamp
      return True
    else:
      return False