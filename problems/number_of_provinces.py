from typing import List


class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    visit = set()  
    adj = {}
    self.getGraph(adj, isConnected)
    cnt = 0
    for i in range(len(isConnected)):
      if i not in visit:
        self.dfs(i, adj, visit)
        cnt += 1
    return cnt

  def getGraph(self, adj,isConnected ):
    m = len(isConnected)
    n = len(isConnected[0])
    for i in range(m):
      for j in range(n):
        if isConnected[i][j]:
          neis = adj.get(i, [])
          neis.append(j)
          adj[i] = neis

          neis = adj.get(j, [])
          neis.append(i)
          adj[j] = neis
          
  def dfs(self, node, adj, visit):
    # base case
    if node in visit:
      return
    
    # recursive rule
    visit.add(node)
    for nei in adj.get(node, []):
      self.dfs(nei, adj, visit)