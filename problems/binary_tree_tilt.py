# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findTilt(self, root: Optional[TreeNode]) -> int:
    self.sum = 0
    self.dfs(root)
    return self.sum
  
  # return sum of tree
  def dfs(self, root)->int:
    if not root:
      return 0
        
    left = self.dfs(root.left)
    right = self.dfs(root.right)
    self.sum += abs(left - right)

    return left + right + root.val