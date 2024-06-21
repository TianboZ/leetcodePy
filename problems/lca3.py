# Definition for a k-nary tree node.
class KnaryTreeNode(object):
    def __init__(self, key):
        self.key = key
        self.children = list()
           
class Solution(object):
  def lowestCommonAncestor(self, root, nodes):
    """
    :type root: KnaryTreeNode
    """
    # nodes  = set(nodes)
    return self.lca(root, nodes)

  def lca(self, root, nodes):
    # base case
    if not root: return None

    if root in nodes:
      return root

    # recursive rule
    cnt = 0
    tmp = None
    for nei in root.children:
      res = self.lca(nei, nodes)
      if res:
        cnt += 1
        tmp = res
      if cnt > 1: # tmp is at least a parent of 2 nodes
        return root
    
    return tmp

