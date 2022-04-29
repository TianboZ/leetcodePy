class Solution:
  def isBipartite(self, graph) -> bool:
    visit = {} # key: node  val: 0 or 1
    
    # return true is is bipartile
    def dfs(node, color):
      # base case
      if node in visit:
        if visit[node] != color: return False
        return True
        
      # recursive rule
      visit[node] = color
      neis = graph[node]
      for nei in neis:
        if not dfs(nei, -color): return False
      
      return True
    
    
    for i in range(len(graph)):
      if i not in visit and not dfs(i, 1): return False
    
    return True
        
    