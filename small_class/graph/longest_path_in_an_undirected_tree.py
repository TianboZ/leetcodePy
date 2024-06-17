"""
MHT question

https://www.geeksforgeeks.org/longest-path-undirected-tree/

"""
from collections import deque
from operator import le


class Solution:
  def getLongestPath(self, node, adj: dict):
    # get any node, run BFS
    leaf, dis = self.bfs(node, adj)

    # run BFS 2nd time from leaf, find longest path
    leaf2, dis = self.bfs(leaf, adj)

    print('leaf to leaf: ', leaf, leaf2, 'dis: ', dis)

  def bfs(self, node, adj):
    print('input node', node)
    visit = set()
    queue = deque([])
    level = 0
    leaf = None

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
        print(curr)
        
        # generate
        for nei in adj.get(curr):
          if nei not in visit:
            queue.append(nei)
            visit.add(nei)
      
      print('level: ', level)
      level += 1
      
    
    print(leaf)
    return [leaf, level]


sol = Solution()
adj = {
  0: [1],
  1: [0, 2, 3],
  2: [1],
  3: [1]
}

adj2 = {
  0: [1],
  1: [0, 2, 6],
  2: [1,9, 3, 4],
  3: [2],
  4: [2, 5],
  5: [4],
  6: [7,8, 1],
  7: [6],
  8: [6],
  9: [2]
  
}
sol.getLongestPath(0, adj2)

