from collections import deque

TIME = 10

class Solution:
  def __init__(self) -> None:
    self.queue = deque([]) # record [timestamp, ip]
    self.map = {} # key: ip   value: [t1, t2, ...]

  def request(self, time, ip):
    self.queue.append([time, ip])
    if ip in self.map:
      self.map.get(ip).append(t)
    else:
      self.map[ip] = [time]

  def checkBotInStream(self, time, limit):
    while self.queue:
      if time - self.queue[0] >= TIME:
        self.queue.popleft()
      else:
        break



  def detectBot(self, log, cnt: int):
    map = {}  # key: ip   value: [t1, t2, ....]
    for t, ip in log:
      if ip in map:
        map.get(ip).append(t)
        if len(map.get(ip)) > cnt:
          print('bot ip:', ip)
          return False
      else:
        map[ip] = [t]
      


sol = Solution()
log = [['1', 'ip1'], ['2', 'ip2'],['3', 'ip3'],['4', 'ip4'],['5', 'ip3'], ['6', 'ip3']]
sol.detectBot(log, 2)
