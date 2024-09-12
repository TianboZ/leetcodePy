from typing import Optional
from problems.UtilityClasses import TreeNode


class Solution:
  def longestConsecutive(self, root: Optional[TreeNode]) -> int:
    self.res = 1
    self.dfs(root)
    return self.res
  
  # return [longestIncreasingPath, longestDecreasingPath] 
  def dfs(self, root)->list[int]:
    # base case
    if not root:
      return [0, 0]
    
    if not root.left and not root.right:
      # leaf node
      return [1, 1]
    
    # recursive rule
    leftInc, leftDec = self.dfs(root.left)
    rightInc, rightDec = self.dfs(root.right)
    
    # find local max
    localMax = 1  # /\  or / or \
    
    # find local parent to child path, / or \
    localMaxInc = 1
    localMaxDec = 1
    
    # left
    if root.left:
      if root.left.val + 1 == root.val:
        localMax = max(localMax, leftDec + 1)
        localMaxDec = max(localMaxDec, leftDec + 1)
    
      if root.left.val - 1 == root.val:
        localMax = max(localMax, leftInc + 1)
        localMaxInc = max(localMaxInc, leftInc + 1)
      
    # right
    if root.right:
      if root.right.val - 1 == root.val:
        localMax = max(localMax, rightInc + 1)
        localMaxInc = max(localMaxInc, rightInc + 1)
      
      if root.right.val + 1 == root.val:
        localMax = max(localMax, rightDec + 1)
        localMaxDec = max(localMaxDec, rightDec + 1)
      
    # /\
    if root.left and root.right:
      if root.left.val + 1 == root.val and root.val + 1 == root.right.val:
        localMax = max(localMax, leftDec + 1 + rightInc)
        
      if root.left.val - 1 == root.val and root.val - 1 == root.right.val:
        localMax = max(localMax, leftInc + 1 + rightDec)
    
    # update global max
    self.res = max(self.res, localMax, localMaxDec, localMaxInc)
    
    return [localMaxInc, localMaxDec]
    
    
    