class Solution(object):
  def lowestCommonAncestor(self, one, two):
    """
    input: TreeNodeP one, TreeNodeP two
    return: TreeNodeP
    """
    # write your solution here
    # find all nodes from one -> root
    path = set()
    curr = one
    while curr:
      path.add(curr)
      curr = curr.parent
    
    # find all nodes from two -> root, if the node in path, then that node is LCA
    curr = two
    while curr:
      if curr in path:
        return curr 
      curr = curr.parent
    
    return None
