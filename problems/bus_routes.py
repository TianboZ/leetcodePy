"""
workable solution:
DFS3

"""
from collections import defaultdict, deque
from typing import List


class Solution:
  def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    # bus that have stop at source
    bus = []
    # build graph
    adj = defaultdict(list)
    for i in range(len(routes)):
      route = routes[i]
      for j in range(len(route)):
        s = route[j]
        # find bus 
        if s == source:
          bus.append(i)
        
        if j + 1 < len(route):
          nextS = route[j + 1]
          adj[s].append([nextS, i])  # [next stop, bus id]
        if j - 1 >= 0:
          prevS = route[j - 1]
          adj[s].append([prevS, i])
    print(adj)
    
    if not bus:
      # source is not valid bus stop
      return -1

    if source == target:
      return 0
    
    self.res = 100

    # run DFS from source
    for b in bus:
      visit = set()
      path = []
      self.dfs(source, b, target, adj, visit, path)
    
    if self.res == 100:
      # not found 
      return -1
    return self.res
  
  # bus is bus index
  # path to record how what bus we take [1, 1, 1, 2, 1, 2, 3...]
  def dfs(self, stop, bus, target, adj, visit, path):
    # base case

    # recursive rule
    if (stop == target):
      print(path + [bus])
      cnt = set(path + [bus])
      print(cnt)
      self.res = min(self.res, len(cnt))
      return    
    
    visit.add(stop)
    path.append(bus)

    for nei in adj.get(stop):
      # [nextStop, bus]
      nextStop, nextBus = nei
      if nextStop not in visit:
        self.dfs(nextStop, nextBus, target, adj, visit, path)
    visit.remove(stop)
    path.pop()

class Solution2:
  def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    if source == target:
      return 0

    adj = defaultdict(list) # <stop: [route_id1, route_id2]>
    for i, r in enumerate(routes):
      for stop in r:
        adj[stop].append(i)
    
    print(adj)
    
    queue = deque([])
    visit = set() # record routeId
    dis = 0
    
    # init 
    for routeId in adj.get(source, []):
      queue.append(routeId)
      visit.add(routeId)
    
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand
        currId = queue.popleft() # route id
        
        # generate
        for stop in routes[currId]:
          # find target
          if stop == target:
            return dis + 1
          
          for nextId in adj.get(stop, []):  # next route id
            if nextId not in visit:
              visit.add(nextId)
              queue.append(nextId)
            
      dis += 1
    
    return -1
      
# test
routes = [[1,2,7],[3,6,7]]
source = 1
target = 6
sol = Solution2()
res = sol.numBusesToDestination(routes, source, target)
print(res)
        