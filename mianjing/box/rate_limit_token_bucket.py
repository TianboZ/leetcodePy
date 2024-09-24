import time


class TokenBucket:
  def __init__(self, size, refillRate) -> None:
    self.tokens = size
    self.size = size
    self.refillRate = refillRate
    self.prevRefillTime = time.time()
    
  def refill(self):
    now  = time.time()
    timePassed = now - self.prevRefillTime
    refillTokens = timePassed * self.refillRate
    self.tokens = min(self.size, self.tokens + refillTokens)
    
    # update
    self.prevRefillTime = now
    
  def handleRequest(self, consumeTokens):
    self.refill()
    print('left tokens:', self.tokens)
    
    if self.tokens >= consumeTokens:
      self.tokens -= consumeTokens
      return True
    else:
      return False
    
#test
rl = TokenBucket(10, 1)
for i in range(15):
  if rl.handleRequest(1):
    print('request:', i, 'handled')
  else:
    print('request:', i, 'rejected')
    
  time.sleep(0.3)