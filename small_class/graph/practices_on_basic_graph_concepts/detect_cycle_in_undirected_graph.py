
'''
OJ:
https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

'''

def if_undirected_graph_has_cycle(adj: dict[int, list[int]]):
  nodes = adj.keys()
  visit = set()
  for n in nodes:
    print(n)
    if n not in visit and  dfs(adj, n, None, visit):
      return True
  return False
  
# detect if has cycle, return true if has cycle
def dfs(adj: dict, node, prev, visit: set) -> bool: 
  # base case
  if node in visit: 
    print(node, prev)
    return True

  # recursive rule
  visit.add(node)
  
  for nei in adj.get(node, []):
    if nei != prev:  
      if dfs(adj, nei, node, visit):
        return True
  return False

# test
# [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]

adj = {
  0: [1],
  1: [0, 2, 4],
  2: [1, 3],
  3: [2, 4],
  4: [1, 3]
}
print(if_undirected_graph_has_cycle(adj))
  