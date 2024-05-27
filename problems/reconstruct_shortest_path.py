from collections import defaultdict, deque

'''
xiaoban

adj = {
  1: [2, 4]
  2: [3]
  3: [1]
  4: [4]
}

given this graph, find and shortest path, e.g. 1->2->3 or 1->4->3

'''


def getAnyPath(adj, src, end):
  queue = deque([])
  visit=set()
  prev = {} # key: current node, val: parent node

  # inital
  queue.append(src)
  visit.add(src)
  prev[src] = None

  # terminate
  while queue:
    # expand
    curr = queue.popleft()
    if curr == end:
      break

    # generate
    for nei in adj.get(curr):
      if nei not in visit:
        visit.add(nei)
        queue.append(nei)
        prev[nei] = curr

  
  # generate shortest path
  curr = end
  path = []
  while curr:
    path.append(curr)
    curr = prev.get(curr)
  
  path.reverse()

  print(path)

# test
print('any shortest path')
adj = {
  1: [2, 4],
  2: [3],
  3: [1],
  4: [4]
}
getAnyPath(adj, 1, 3)


'''
adj = {
  1: [2, 4]
  2: [3]
  3: [1]
  4: [4]
}

given this graph, find all shortest path, e.g. 1->2->3 and 1->4->3

'''
class Solution:
  def getAllPaths(self, adj, src, end):
    queue = deque([])
    visit=set()
    prev = {} # <node, parent node>
    levels = {}  # <node, level>
    level = 0
    
    # inital
    queue.append(src)
    visit.add(src)
    prev[src] = [None]
    levels[src] = 0

    # terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand
        curr = queue.popleft()

        # generate
        for nei in adj.get(curr):
          if nei not in visit:
            visit.add(nei)
            levels[nei] = level + 1
            queue.append(nei)
            prev[nei] = [curr]
          elif level + 1 == levels.get(nei): # Check for the same shortest path length
            prev.get(nei).append(curr)
      
      if end in levels:
        break
      level =+ 1
    print(prev)

    # print all paths
    res = []
    path = []
    self.dfs(end, src, path, res, prev)
    print(res)

  def dfs(self, node, target, path, res, prev):
    #  base case

    # recursive rule
    path.append(node)
    
    if node == target:
      tmp = path.copy()
      tmp.reverse()
      res.append(tmp)
    
    for nei in prev.get(node, []):
      self.dfs(nei, target, path, res, prev)
    
    path.pop()

#test
print('all shortest path')

adj = {
    1: [2, 3],
    2: [4, 1],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}
sol = Solution()
sol.getAllPaths(adj, 1, 5)
