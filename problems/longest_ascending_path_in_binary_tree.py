# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def longest(self, root):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    self.res = 0
    self.dfs(root)
    return self.res

  # return longest path from root
  def dfs(self, root)->int: 
    # base case
    if not root:
      return 0

    # recursive rule
    left = self.dfs(root.left)
    right = self.dfs(root.right)
    localmax = 1
    if root.left and root.left.val > root.val:
      localmax = max(localmax, left + 1)
    if root.right and root.right.val > root.val:
      localmax = max(localmax, right + 1)

    self.res = max(self.res, localmax)
    return localmax
