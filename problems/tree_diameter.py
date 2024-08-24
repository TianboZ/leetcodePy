from typing import List
from collections import deque, defaultdict

class Solution:
  def treeDiameter(self, edges: List[List[int]]) -> int:
    # build adj list graph
    adj= defaultdict(list)
    for e in edges:
      a, b = e
      adj[a].append(b)
      adj[b].append(a)
    
    dstNode, dis = self.bfs(0, adj)
    _, dis = self.bfs(dstNode, adj)

    print( dis)
    return dis
  
  # find the farthest node and distance, return e.g. [node, dis]
  def bfs(self, node, adj)->List[int]:
    visit = set()
    dis = -1
    queue = deque([])   # e.g.  [  [node, preNode], [node2, preNode2], ...  ]   
    dstNode = None
    
    # init
    queue.append([node, None])
    visit.add(node)

    # terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand
        curr = queue.popleft()
        currNode, preNode = curr
        dstNode = currNode
        print('bfs:', dstNode)

        # generate
        neis = adj.get(currNode, [])
        for nei in neis:
          if nei != preNode and nei not in visit:
            queue.append([nei, currNode])
            visit.add(nei)
      dis += 1
    
    return [dstNode, dis]
  
sol = Solution()
e = [[0,1],[1,2],[2,3],[1,4],[4,5]]
sol.treeDiameter(e)
