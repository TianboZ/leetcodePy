import math
from typing import Optional
from UtilClass import *

class Solution:
  # sol1
  prev = -math.inf

  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    if not root: return True
    
    left = self.isValidBST(root.left)
    if not left: return False
    if root.val <= self.prev: return False
    self.prev = root.val
    return self.isValidBST(root.right)

  # sol2
  def isValidBST(self, root):
    return self.helper(root, -math.inf, math.inf)

  def helper(self, root, lo, hi):
    if not root: return True

    if root.val <= lo or root.val >= hi: return False
    return self.helper(root.left, lo, root.val) and self.helper(root.right, root.val, hi) 


