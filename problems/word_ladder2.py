from collections import deque, defaultdict
from typing import List

class Solution:
  def findLadders(
    self, beginWord: str, endWord: str, wordList: List[str]
  ) -> List[List[str]]:
    self.res = []
    if endWord not in wordList:
      return []

    # build adj graph
    adj = self.getGraph(wordList)

    print(adj)
    # get shortest distance
    self.depth = self.bfs(adj, beginWord, endWord) 
    
    # run depth limited DFS
    path = []
    visit = set()
    self.target = endWord
    self.dfs(beginWord, 0, path, visit, adj)

    return self.res

  # run depth limited DFS, find all paths
  def dfs(self, node, depth, path, visit, adj):
    # base case
    if node in visit:
      return 

    if depth == self.depth - 1:
      if node == self.target:
        self.res.append(list(path) + [node])
        print(path + [node])
      return

    # recursive rule
    visit.add(node)
    path.append(node)
    for nei in adj.get(node, []):
      self.dfs(nei, depth + 1, path, visit, adj)
    visit.remove(node)
    path.pop()
          
  def getGraph(self, words):
    adj = defaultdict(list)
    for w in words:
      for w2 in words:
        if w == w2:
          continue
        
        if len(w) != len(w2):
          continue
        
        # count how many chars are diff
        i = 0
        cnt = 0
        while i < len(w):
          c1 = w[i]
          c2 = w2[i]
          if c1 != c2:
            cnt += 1
          if cnt > 1:
            break
            
          i += 1
        
        if i == len(w) and cnt == 1:
          adj[w].append(w2)
  
    print(adj)    
    return adj
      
  def bfs(self, adj, start, target):
    queue = deque([])
    visit = set()
    dis = 0
    
    # init
    queue.append(start)
    visit.add(start)
    
    #  terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        #   expand
        curr = queue.popleft()
        
        if curr == target:
          return dis + 1
          # print(dis)
        
        # generate
        for nei in adj.get(curr, []):
          if nei not in visit:
            queue.append(nei)
            visit.add(nei)
      dis += 1
    
    return 0, []
            
"""
WRONG! 
while BFS, record prev <node: parent node>, but it will only generate one valid solution

"""
class Solution2:
  def findLadders(
    self, beginWord: str, endWord: str, wordList: List[str]
  ) -> List[List[str]]:
    self.res = []
    if endWord not in wordList:
      return []

    # build adj graph
    adj = self.getGraph( wordList)
    

    print(adj)
    # get shortest distance
    depth, prev = self.bfs(adj, beginWord, endWord) 
    print(depth, prev)
    
    # run DFS on prev map, find all path, then reverse the path
    self.dfs(endWord, prev, [], beginWord)

  def dfs(self, node, prev, path, target):
    # base case
    
    # recursive rule
    path.append(node)
    if node == target:
      print(path)
      path.pop()
      return
    
    for nei in prev.get(node, []):
      self.dfs(nei, prev, path, target)
    
    path.pop()
      
  # return 
  def bfs(self, adj, start, target):
    queue = deque([])
    visit = set()
    dis = 0
    prev = defaultdict(list) # key: node, value: parent nodes
    
    # init
    queue.append(start)
    visit.add(start)
    prev[start] = []
    
    #  terminate
    while queue :
      size = len(queue)
      for _ in range(size):
        #   expand
        curr = queue.popleft()
        
        if curr == target:
          return dis + 1, prev # will miss some solution, only return any one valid path, not all
        
        # generate
        for nei in adj.get(curr, []):
          if nei not in visit:
            queue.append(nei)
            visit.add(nei)
            prev[nei].append(curr)
      dis += 1
    
    # print(2)
    # print(prev)
    return 0, []
       
       
  def getGraph(self, words):
    adj = defaultdict(list)
    for w in words:
      for w2 in words:
        if w == w2:
          continue
        
        if len(w) != len(w2):
          continue
        
        # count how many chars are diff
        i = 0
        cnt = 0
        while i < len(w):
          c1 = w[i]
          c2 = w2[i]
          if c1 != c2:
            cnt += 1
          if cnt > 1:
            break
            
          i += 1
        
        if i == len(w) and cnt == 1:
          adj[w].append(w2)
  
    print(adj)    
    return adj
      


# test
sol = Solution2()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
res = sol.findLadders(beginWord, endWord, wordList)
print(res)
