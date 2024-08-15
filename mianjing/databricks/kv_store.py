from collections import deque
import time


"""
queue store tuple, (timestamp, count). more efficient for repeat timestmap

follow up: 精度处理
"""

TIME_RANGE = 300 

class KeyValueStore:
  def __init__(self, generateTime = None) -> None:
    self.getQueue = deque([])
    self.putQueue = deque([])
    self.map = {}
    self.getTotal = 0
    self.putTotal = 0
    self.generateTime = generateTime

  def getTime(self):
    if self.generateTime:
      return self.generateTime()
    
    return round(time.time(), 5)   # seconds
  
  def put(self, key, val):
    currTime = self.getTime()
    if self.putQueue and self.putQueue[-1][0] == currTime:
      prevCnt = self.putQueue[-1][1]
      self.putQueue.pop()
      self.putQueue.append((currTime, prevCnt + 1))
    else:
      self.putQueue.append((currTime,1))

    self.map[key] = val
    self.putTotal += 1

  def get(self, key):
    currTime = self.getTime()
    if self.getQueue and self.getQueue[-1][0] == currTime:
      prevCnt = self.getQueue[-1][1]
      self.getQueue.pop()
      self.getQueue.append((currTime, prevCnt + 1))
    else:
      self.getQueue.append((currTime,1))

    self.getTotal += 1
    
    return self.map.get(key, None)

  # average times per second that put/get function be called 
  # within past 5 minutes‍‌‌‍‌‍‍‍‍‍‌‍‌‌‌‌‌‌，就是当前时间的前五分钟内，平均每秒钟put/get 
  # 被调用的次数
  def measure_put_load(self):
    currTime = self.getTime()
    while self.putQueue:
      if currTime - self.putQueue[0][0] > TIME_RANGE:
        print('pop')
        self.putTotal = self.putTotal - self.putQueue[0][1]
        self.putQueue.popleft()
      else:
        break
    
    print(self.putQueue)
    print(self.putTotal)
    return self.putTotal / TIME_RANGE


  def measure_get_load(self):
    pass
  

# print(time.time())

x = 0
def generateTime():
  return time.time() + x

map = KeyValueStore(generateTime)

# for _ in range(100):
#   map.put(1, 100)
#   map.get(2)

# print(map.measure_put_load(), map.putTotal)

map.put(1, 1)
print(map.measure_put_load())

x = 300
map.put(1,1)
map.put(1,1)
map.put(1,1)

print(map.measure_put_load())


x=1000
for _ in range(100):
  map.put(1, 100)
print(map.measure_put_load())




