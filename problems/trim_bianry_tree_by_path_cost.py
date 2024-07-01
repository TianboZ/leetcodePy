# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def trimTree(self, root, k):
    """
    input: TreeNode root, int k
    return: TreeNode
    """
    # write your solution here
    if not root:
      return None
    
    return self.dfs(root, 0, k)
    
  
  # return root of trimmed binary tree
  def dfs(self, root, level, k):
    if not root:
      return None

    left = self.dfs(root.left, level + 1, k)
    right = self.dfs(root.right, level + 1, k)
    
    root.left = left
    root.right = right

    if not root.left and not root.right and level < k - 1:
      # leaf node
      return None
    
    return root
