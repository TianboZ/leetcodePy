from collections import deque
import time

TIME_RANGE = 300 

class KVStore:
  def __init__(self, getTime) -> None:
    self.map = {}
    self.putQueue = deque([])  # item in queue is pair of (timestamp, count)
    self.getQueue = deque([])
    self.putTotal = 0
    self.getTotal = 0
    self.customGetTime = getTime
    
  def getTime(self):
    if self.customGetTime:
      return self.customGetTime()
    return time.time()
  
  def put(self, key, val):
    self.map[key] = val
    self.putTotal += 1
    now = self.getTime()

    if self.putQueue and self.putQueue[-1][0] == now:
      self.putQueue[-1][1] = self.putQueue[-1][1] + 1
    else:
      self.putQueue.append([now, 1])

  def get(self, key):
    res = self.map.get(key, None)
    self.getTotal += 1
    now = self.getTime()
    
    if self.getQueue and self.getQueue[-1][0] == now:
      self.getQueue[-1][1] = self.getQueue[-1][1] + 1
    else:
      self.getQueue.append([now, 1])

    return res


  def putQPS(self):
    now = self.getTime()
    print('putqueue', self.putQueue)

    while self.putQueue:
      if now - self.putQueue[0][0] > TIME_RANGE:
        self.putTotal = self.putTotal - self.putQueue[0][1]
        self.putQueue.popleft()
      else:
        break
    return self.putTotal / TIME_RANGE

  def getQPS(self):
    now = self.getTime()
    print('getqueue', self.getQueue)
    while self.getQueue:
      if now - self.getQueue[0][0] > TIME_RANGE:
        self.getTotal = self.getTotal - self.getQueue[0][1]
        self.getQueue.popleft()
      else:
        break
    return self.getTotal / TIME_RANGE

# test 
x = 0
def customGetTime():
  return round(time.time(), 4) + x


kvStore = KVStore(customGetTime)
x = 0
for _ in range(10):
  kvStore.put(1, 1)
  kvStore.get(1)

x = 200
kvStore.get(1)
kvStore.put(1, 2)
kvStore.put(1, 2)


print(kvStore.getQPS())  # 11/300 = 0.03666
print(kvStore.putQPS())  # 12/300  = 0.04
# print(kvStore.get(1))

x = 505
print(kvStore.getQPS())  # 0
print(kvStore.putQPS())  # 0


# y = 0
# def func():
#   return 1 + y

# print(func())
# y += 1
# print(func())
# y += 1
# print(func())
