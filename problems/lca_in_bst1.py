# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def lca(self, root, p, q):
    """
    input: TreeNode root, int p, int q
    return: TreeNode
    """
    # write your solution here
    return self.helper(root, p, q)
  
  def helper(self, root, a, b):
    # base case
    if not root: 
      return None
    if a == root.val or b == root.val:
      return root
    
    # recursive rule
    if a > root.val and b > root.val:
      return self.helper(root.right, a, b)
    if a < root.val and b < root.val:
      return self.helper(root.left, a, b)
    
    return root
