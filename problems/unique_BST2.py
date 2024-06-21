# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from UtilityClasses import *

class Solution:
  def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    min = 1
    max = n
    res = self.dfs(min, max)
    return res
  
  # [lo, hi] is BST value range, min, max is global range. dfs function
  # returns array of root
  # res stores all BST root
  def dfs(self, min, max)->List[TreeNode]:
    # base case
    if min > max: return [None]

    # recursive rule
    res = []
    for v in range(min, max + 1):
      
      leftNodes = self.dfs(min, v - 1 )
      rightNodes = self.dfs(v + 1, max)
      for left in leftNodes:
        for right in rightNodes:
          root = TreeNode(v)
          root.left = left
          root.right = right
          res.append(root)
    
    return res
  
# test
sol = Solution()
res = sol.generateTrees(3)
print(res)

