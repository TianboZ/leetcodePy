"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


solution:

time
O(V + E)
space
O(V)
"""
from UtilityClasses import Node
from typing import Optional
class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    # sanity check
    visit = {}
    return self.dfs(node, visit)

  # input node, return cloned node
  def dfs(self, node, visit: dict):
    # base case
    if not node:
      return None

    if node in visit:
      return visit.get(node)

    # recursive rule
    copy = Node(node.val, [])
    visit[node] = copy

    for nei in node.neighbors:
      copy.neighbors.append(self.dfs(nei, visit))
    return copy
  
# test
sol = Solution()
n1 = Node(1)
n4 = Node(4)
n2 = Node(2)
n3 = Node(3)

n1.neighbors = [n2,n3]
n2.neighbors = [n1]
n3.neighbors = [n4, n1]
n4.neighbors = [n3, n1]

n11 = sol.cloneGraph(n1)
seen = set()
map = {}

def print_graph(node: Node):
  if not node: 
    return None
  
  if node.val in seen: 
    return node.val

  seen.add(node.val)
  val = node.val
  map[val] = []
  for nei in node.neighbors:
    map[val].append(print_graph(nei))
  return val


print_graph(n11)

print(map)