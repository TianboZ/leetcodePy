from collections import deque
import time

class LeakyBucket:
  def __init__(self, size, leakRate) -> None:
    self.size = size
    self.bucket = deque([])
    self.leakRate = leakRate
    self.prevLeakTime = time.time()
    self.leakAcc = 0 # keep track of fraction part
    
  def leak(self):
    now = time.time()
    timePassed = now  - self.prevLeakTime
    leaksCnt = timePassed * self.leakRate + self.leakAcc
    leaksCntInt  = int(leaksCnt)
    
    # leak accmulated request
    for _ in range(leaksCntInt):
      if self.bucket:
        self.bucket.popleft()
      else:
        break
    
    # update
    self.prevLeakTime = now
    self.leakAcc = leaksCnt - leaksCntInt
    
  # return true if the request can be handled
  def handleRequest(self, req):
    self.leak()
    if len(self.bucket) < self.size:
      self.bucket.append(req)
      return True
    else:
      return False
    
# test 
rl = LeakyBucket(5, 1)
for i in range(20):
  if rl.handleRequest(i):
    print('request: ', i, 'handled')
  else:
    print('request: ', i, 'rejected')
  
  time.sleep(0.3)