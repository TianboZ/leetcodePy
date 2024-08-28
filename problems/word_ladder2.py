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
    adj = defaultdict(set)
    self.getAdj(beginWord, endWord, wordList, adj)

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

  def getAdj(self, begin, end, words, adj):
    words.insert(0, begin)
    for w in words:
      for w2 in words:
        if w == w2:
          continue
        if self.isOneCharDiff(w, w2):
          adj[w].add(w2)
          adj[w2].add(w)
      
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
    
    return 0
            
      
  def isOneCharDiff(self, s1, s2):
    if len(s1) != len(s2):
      return False
    cnt = 0
    # print(s1)
    for i in range(len(s1)):
      if s1[i] != s2[i]:
        cnt += 1
        if cnt > 1:
          return False
    return True


# test
sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
res = sol.findLadders(beginWord, endWord, wordList)
print(res)

