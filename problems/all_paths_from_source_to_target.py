from typing import List

"""
solution:
1. DFS3, mark visited 3
most straight forward method

time: O(b^level)
space: O(level)

"""

class Solution:
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    path = []
    res = []
    self.dfs(graph, 0, path, res, len(graph) - 1)
    return res

  def dfs(self, graph, node, path, res, target):
    # base case
    if node == target:
      res.append(list(path) + [node])
      return

    # recursive rule
    path.append(node)
    for nei in graph[node]:
      self.dfs(graph, nei, path, res, target)
    path.pop()

sol = Solution()
res = sol.allPathsSourceTarget([[1,2],[3],[3],[]])
print(res)

