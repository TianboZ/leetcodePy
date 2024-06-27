# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution(object):
  def diameter(self, root):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    if not root:
      return 0
    self.res = 0
    self.dfs(root)
    return self.res

  # return root to leaf dis
  def dfs(self, root)->int:
    # base case
    if not root: return 0

    # recursive rule
    left = self.dfs(root.left)
    right = self.dfs(root.right)
    if root.left and root.right:
      self.res = max(self.res, left + right + 1)
    return max(left, right) + 1