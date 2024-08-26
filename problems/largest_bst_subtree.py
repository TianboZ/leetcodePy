"""
solution:
- DFS traverse tree, DFS return [lo, hi, size]
  - [lo, hi] is valid range when root is BST, size is subtree size 

complexity:
time O(N)
space O(tree height) = O(N) worst case

"""
import math
class Solution2:
  def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
    self.maxsize  = 0
    self.maxval = 10000000
    self.dfs(root)
    return self.maxsize

  # returns [lo, hi, subtree_size] 
  def dfs(self, root):
    # base case
    if not root:
      # [inf, -inf] is valid BST, size is 0
      return [self.maxval, -self.maxval, 0]

    # recursive rule
    left = self.dfs(root.left)
    right = self.dfs(root.right)

    leftLo, leftHi, leftSize = left
    rightLo, rightHi, rightSize = right

    if leftHi < root.val < rightLo:
      # current root is BST
      localMax = leftSize + rightSize + 1
      print(localMax)
      self.maxsize = max(self.maxsize, localMax)
      """
          5
           \
           8
      in this case, 5 is BST, 5.left subtree is empty, returns [inf, -inf], leftLo is inf
      """
      return [min(leftLo, root.val), max(rightHi, root.val), localMax]

    # return [-inf, inf] so parent can't be BST 
    return [-self.maxval, self.maxval, 0]
  

"""
solution:
complexity
O(N^2)

soluiton2:
O(N)
"""

import math
from typing import Optional
from problems.UtilityClasses import TreeNode


class Solution:
  def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
    self.maxBST  = 0
    self.traverse(root)
    # self.dfs(root, -math.inf, math.inf)
    return self.maxBST

  def traverse(self, root):
    if not root:
      return

    self.dfs(root, -math.inf, math.inf)
    self.traverse(root.left)
    self.traverse(root.right)

  # (lo, hi) is BST range
  def dfs(self, root, lo, hi)->[bool, int]:
    if not root:
      return [True, 0]

    if root.val <= lo or root.val >= hi:
      return [False, 0]

    left = self.dfs(root.left, lo, root.val)
    right = self.dfs(root.right, root.val, hi)

    # left and right subtree are all valid BST
    if left[0] and right[0]:
      self.maxBST = max(self.maxBST, left[1] + right[1] + 1)
      return [True, left[1] + right[1] + 1]
    
    return [False, 0]
  

