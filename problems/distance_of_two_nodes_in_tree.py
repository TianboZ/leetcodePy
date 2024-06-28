"""
solution:
- find LCA of 2 nodes
- traverse from LCA node, until reach 2 nodes, record distance
"""

from UtilityClasses import TreeNode

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  def distance(self, root, k1, k2):
    lca = self.getLCA(root, k1, k2)
    self.dis = 0
    self.getDistance(lca, k1, k2, 0)
    return self.dis

  # level is tree depth
  def getDistance(self, root, a, b, level):
    if not root:
      return 
    
    if root.val == a or root.val == b:
      self.dis += level
    
    self.getDistance(root.left, a, b, level + 1)
    self.getDistance(root.right, a, b, level + 1)

  def getLCA(self, root, a, b) -> TreeNode:
    # base case
    if not root or root.val == a or root.val == b:
      return root

    # recursive rule
    left = self.getLCA(root.left, a, b)
    right = self.getLCA(root.right, a, b)

    if left and right:
      return root
    
    if not left:
      return right
    return left
    