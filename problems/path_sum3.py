from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    self.res = 0
    map = {} # key: prefix sum value     value: frequency
    self.dfs(root, 0, targetSum, map)
    return self.res

  def dfs(self, root, sum, target, map: dict):
    if not root:
      return
    
    currSum = sum + root.val
    if currSum == target:
      self.res += 1
  
    if currSum - target in map:
      self.res = self.res + map.get(currSum - target)

    # add current sum after count!
    map[currSum] = map.get(currSum, 0) + 1

    self.dfs(root.left, currSum, target, map)
    self.dfs(root.right, currSum, target, map)

    # backtracking
    map[currSum] = map.get(currSum) - 1