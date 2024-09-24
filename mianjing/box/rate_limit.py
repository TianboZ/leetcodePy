'''
token bucket 
'''


"""
leak bucket
"""
import time
from collections import deque

class LeakyBucket:
  def __init__(self, capacity, leak_rate):
    """
    Initializes the leaky bucket.
    :param capacity: Maximum number of requests the bucket can hold.
    :param leak_rate: Number of requests that can be processed per second.
    """
    self.capacity = capacity
    self.leakRate = leak_rate
    self.bucket = deque()
    self.lastLeakTime = time.time()
    self.reqToLeakAcc = 0  # Tracks partial leaks

  def leak(self):
    """
    Leaks (processes) requests based on the elapsed time since the last check.
    """
    currTime = time.time()
    timePassed = currTime - self.lastLeakTime
    # Calculate how many requests can be processed in the time passed
    reqToLeakTotal = timePassed * self.leakRate + self.reqToLeakAcc
    
    # Leak requests based on the whole number portion of requests_to_leak
    reqToLeakCnt = int(reqToLeakTotal)
    
    for _ in range(reqToLeakCnt):
      if self.bucket:
        self.bucket.popleft()
      else:
        break
    
    # Save the fractional part of requests_to_leak for future leaks
    self.reqToLeakAcc = reqToLeakTotal - reqToLeakCnt
    # Update the last check time
    self.lastLeakTime = currTime

  def add_request(self, request):
    """
    Adds a request to the bucket.
    :param request: Request to be added (could be any object or just a placeholder).
    :return: True if the request is accepted, False if it is rejected due to bucket overflow.
    """
    # Leak the bucket before adding a new request
    self.leak()
    if len(self.bucket) < self.capacity:
      self.bucket.append(request)
      return True
    else:
      # Bucket is full, request is rejected
      return False


# Example usage
bucket = LeakyBucket(capacity=5, leak_rate=1)  # Bucket can hold 5 requests, leaks 1 request per second

for i in range(20):
  if bucket.add_request(f"Request {i}"):
    print(f"Accepted Request {i}")
  else:
    print(f"Rejected Request {i}")
  time.sleep(0.3)  # Simulate time between requests
