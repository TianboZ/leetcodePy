"""
workable solution:
DFS3

"""
from collections import defaultdict, deque
from typing import List


class Solution2:
  def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    if source == target:
      return 0

    adj = defaultdict(list) # <stop_id: [bus_id1, bus_id2...]>
    for i, r in enumerate(routes):
      for stopid in r:
        adj[stopid].append(i)
    
    print(adj)
    
    queue = deque([])
    visit = set() # record busid
    dis = 0
    
    # init 
    for busid in adj.get(source, []):
      queue.append(busid)
      visit.add(busid)
    
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand
        currId = queue.popleft() # busid
        
        # generate
        for stopid in routes[currId]:
          # find target
          if stopid == target:
            return dis + 1
          
          for nextbusid in adj.get(stopid, []): 
            if nextbusid not in visit:
              visit.add(nextbusid)
              queue.append(nextbusid)
            
      dis += 1
    
    return -1
      
# test
routes = [[1,2,7],[3,6,7]]
source = 1
target = 6
sol = Solution2()
res = sol.numBusesToDestination(routes, source, target)
print(res)
        