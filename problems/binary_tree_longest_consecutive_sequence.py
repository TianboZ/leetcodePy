# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def longestConsecutive(self, root):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    self.res = 0
    self.dfs(root)
    return self.res

  def dfs(self, root)->int:
    if not root:
      return 0

    left = self.dfs(root.left)
    right = self.dfs(root.right)

    localmax = 1
    if root.right and root.val + 1 == root.right.val:
      localmax = max(localmax, right + 1)
    if root.left and root.val + 1 == root.left.val:
      localmax = max(localmax, left + 1)

    self.res = max(self.res, localmax)

    return localmax
      