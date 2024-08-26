from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
solution:
prefix sum, DFS traverse the tree, keep track of path info
use map, key is prefix sum (root --> node), value is freq, e.g.
{
  0: 1,
  10: 1,
  7: 1,

}
        10
      /   \  
    5     -3
  / \       \
 3   2      11  
/ \    \
3 -2    1
edge case

      0
    /   \
   1     1
"""

class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    path = {}
    path[0] = 1
    self.cnt = 0
    self.dfs(root, 0, targetSum, path)

    return self.cnt

  def dfs(self, root, preSum, target, path):
    # base case
    if not root:
      return 

    # recursive rule
    currSum = preSum + root.val
    if currSum - target in path:
      self.cnt += path.get(currSum - target )
    
    path[currSum] = path.get(currSum, 0) + 1
    
    self.dfs(root.left, currSum, target, path)
    self.dfs(root.right, currSum, target, path)
    
    # back tracking
    path[currSum] = path.get(currSum) - 1
    if path[currSum] == 0:
      path.pop(currSum)