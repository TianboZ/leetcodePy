# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
soluiton:
return pair [max sum if rob root, max sum not rob root]

complexity:
time O(n)
space O(tree height) = O(logn)

"""

from typing import List, Optional


class Solution:
  def rob(self, root: Optional[TreeNode]) -> int:
    self.res = 0
    self.dfs(root)
    return self.res

  # return max rob sum from subtree, [rob, not rob]
  def dfs(self, root)->List[int]:
    if not root:
      return [0, 0]

    left = self.dfs(root.left)
    right = self.dfs(root.right)

    # rob root
    sum = root.val + left[1] + right[1]

    # not rob root
    sum2 = max(left) + max(right)

    self.res = max(self.res, sum, sum2)
    return [sum, sum2]

    
        