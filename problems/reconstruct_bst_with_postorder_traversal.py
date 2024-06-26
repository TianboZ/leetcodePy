# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from problems.UtilityClasses import TreeNode


class Solution(object):
  def reconstruct(self, post):
    """
    input: int[] post
    return: TreeNode
    """
    # write your solution here
    return self.dfs(post, 0, len(post) - 1)
  
  def dfs(self, post, l, r):
    if l > r:
      return None
    
    rootVal = post[r]
    root = TreeNode(rootVal)
    j = l
    while post[j] < rootVal:
      j += 1

    root.left = self.dfs(post, l, j - 1)
    root.right = self.dfs(post, j, r - 1)

    return root