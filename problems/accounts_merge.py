import collections
from typing import List
class Solution:
  def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    adj = collections.defaultdict(set)
    for acc in accounts:
      for email in acc[2:]:
        adj[email].add(acc[1])
        adj[acc[1]].add(email)
    
    visit = set()
    ans = []
    for acc in accounts:
      name = acc[0]
      email = acc[1]
      res = []
      if email not in visit:
        self.dfs(email, adj, visit, res)
        print(name, res)
        res.sort()
        ans.append([name] + res)
  
    return ans
  
  def dfs(self, node, adj, visit, res):
    if node in visit:
      return

    visit.add(node)
    res.append(node)
    for nei in adj.get(node, []):
      self.dfs(nei, adj ,visit, res)
    