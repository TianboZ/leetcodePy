import math
from typing import Optional

from UtilityClasses import TreeNode

class Solution:
  # sol1
  prev = -math.inf

  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # base case
    if not root: 
      return True

    # recursive rule
    left = self.isValidBST(root.left)
    if not left: 
      return False

    if root.val <= self.prev:
      return False
    
    self.prev = root.val
    right = self.isValidBST(root.right)
    return right

  # sol2
  def isValidBST2(self, root):
    return self.helper3(root, -math.inf, math.inf)

  def helper3(self, root, min, max) -> bool:
    # base case
    if not root: return True

    # recursive rule
    left = self.helper3(root.left, min, root.val)
    right = self.helper3(root.right, root.val, max)
    
    if (not left or not right): return False
    if root.val >= max or root.val <= min: return False

    return True


sol = Solution()

n0 = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)


n2.left = n1
n1.left = n0
n2.right = n3

# n0.right = n4

print(sol.isValidBST2(n2))
