from collections import deque
import collections
from typing import Dict, List

class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    # sanity check
    if not edges: return [0]
    
    adj = collections.defaultdict(list)
    for a, b in edges:
      adj[a].append(b)
      adj[b].append(a)

    leaf, _ = self.bfs(0, adj)
    _, levelToNodes = self.bfs(leaf, adj)

    maxLevel = max(levelToNodes.keys())
    # print(maxLevel)
    # print(map)
    res = []
    if maxLevel % 2 != 0:
      res.append(levelToNodes[maxLevel // 2][0])
      print('levelToNodes', levelToNodes)
      print('levelToNodes[maxLevel/2]', levelToNodes[maxLevel // 2])
      res.append(levelToNodes[maxLevel // 2 + 1][0])
    else:
      res.append(levelToNodes[maxLevel // 2][0])

    # print(res)
    res.sort()
    return res

  # return farthest node and 
  def bfs(self, node, adj)->tuple[int, dict]:
    visit = set()
    queue = deque([])
    level = 0
    leaf = None
    levelToNodes = collections.defaultdict(list)

    # initial
    queue.append(node)
    visit.add(node)

    # terminate
    while queue:
      size  = len(queue)
      for i in range(size):
        # expand
        curr  = queue.popleft()
        leaf = curr
        levelToNodes[level].append(curr)
        # print(curr)
        
        # generate
        for nei in adj.get(curr, []):
          if nei not in visit:
            queue.append(nei)
            visit.add(nei)
      
      level += 1
      
    # print(levelToNodes)
    # print(leaf)
    return [leaf, levelToNodes]
  

sol = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
sol.findMinHeightTrees(n, edges)