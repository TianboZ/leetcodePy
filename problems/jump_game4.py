"""
build graph, run BFS to find shortest path

"""
from collections import defaultdict, deque

class Solution:
  def minJumps(self, arr: List[int]) -> int:
    # build graph
    adj = defaultdict(list) # <index: [index2, index3....]>
    map = defaultdict(list) # <num: index[]>
    for i, n in enumerate(arr):
      map[n].append(i)
    
    for i, n in enumerate(arr):
      j = i + 1
      if j < len(arr):
        adj[i].append(j)
      
      j = i - 1
      if j >= 0:
        adj[i].append(j)
      
      for index in map.get(n):
        if index != i and index != i + 1 and index != i - 1:
          adj[i].append(index)
    print(adj)

    # BFS
    visit = set()
    queue = deque([])
    
    # init 
    queue.append(0)
    visit.add(0)
    dis = 0

    while queue:
      size = len(queue)
      for _ in range(size):
        # expand
        curr = queue.popleft()

        if curr == len(arr) - 1:
          return dis

        # generate
        for nei in adj.get(curr, []):
          if nei not in visit:
            visit.add(nei)
            queue.append(nei)
      dis += 1

    return 1
