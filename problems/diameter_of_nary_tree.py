"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
  def diameter(self, root: 'Node') -> int:
    """
    :type root: 'Node'
    :rtype: int
    """
    self.res = 0
    self.dfs(root)
    return self.res
  
  # find depth of root
  def dfs(self, root)->int:
    if not root: 
      return 0
    
    max1 = 0
    max2 = 0
    for nei in root.children:
      depth  = self.dfs(nei)
      if depth > max1:
        max2 = max1
        max1 = depth
      elif depth > max2:
        max2 = depth
    
    self.res = max(self.res, max1 + max2)
    return max(max1, max2) + 1