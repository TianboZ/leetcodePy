# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    self.res = []
    self.dfs(root, [], 0, targetSum)
    return self.res
  
  def dfs(self, root, path, sum, target):
    if not root:
      return
    
    if not root.left and not root.right:
      # leaf
      if sum + root.val == target:
        path.append(root.val)
        self.res.append(path.copy())
        path.pop()
      return
    
    path.append(root.val)
    self.dfs(root.left, path, sum + root.val, target)
    self.dfs(root.right, path, sum + root.val, target)
    path.pop()
    