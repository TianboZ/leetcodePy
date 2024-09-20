# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional
from problems.UtilityClasses import TreeNode


class Solution:
  def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
    map = {} # key: tree node val, value: freq
    self.dfs(root, map)
    print(map)

    return sum(map.values())
  
  # return true if same value
  def dfs(self, root, map)->bool:
    if not root:
      return True
    
    left = self.dfs(root.left, map)
    right = self.dfs(root.right, map)

    if left and right:
      val = root.val
      if root.left and root.left.val != val:
        return False
      if root.right and root.right.val != val:
        return False
      
      map[val] = map.get(val, 0) + 1
      return True
    else:
      return False