"""
solution:
1. build graph
2. for eath root, get depth. if detect cycle, then return -1

"""


class Solution(object):
  def depth(self, forest):
    """
    input: int[] forest
    return: int
    """
    # write your solution here
    roots = []
    adj = {}
    visit = set()
    nodes = set()
    res = 0

    # get adj ma
    self.getGraph(forest, adj, roots, nodes)
    print(adj)
    print(roots)

    # for each root, get foreset height
    for r in roots:
      depth = self.getHeight(r, adj, visit)  
      if depth == -1: 
        return -1
      res = max(res, depth)
    
    # check if all nodes traversed
    print(' nodes:', nodes, 'visit: ', visit )
    if len(nodes) != len(visit):
      return -1
    
    return res

  def getGraph(self, forest: list[int], adj: dict, roots: list[int], nodes):
    for i in range(len(forest)):
      v = forest[i]
      if v == -1:
        roots.append(i)
        nodes.add(i)
      else:
        neis = adj.get(v, [])
        neis.append(i)
        adj[v] = neis
        nodes.add(v)
        nodes.add(i)

  def getHeight(self, root, adj, visit) -> int:
    # base case
    if root in visit: 
      return -1

    # recursive rule
    depth = 0
    visit.add(root)
    for nei in adj.get(root, []):
      childDepth = self.getHeight(nei, adj, visit)
      if childDepth == -1: 
        return -1  # cycle
      depth = max(depth, childDepth)
    return depth + 1
    



# test
sol = Solution()
# f = [2,2,-1,4,5,6,3]
f = [-1, 0, 1, 2, 3, 4, 5]
depth = sol.depth(f)
print('res: ', depth)