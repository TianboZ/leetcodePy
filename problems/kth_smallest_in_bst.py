from typing import Optional

from UtilityClasses import TreeNode


class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    self.i = 0
    self.cnt = k
    self.res = None
    self.dfs(root)
    return self.res
  
  # inorder traverse, find kth node
  def dfs(self, root):
    if not root or self.i >= self.cnt:
        return

    self.dfs(root.left)
    
    print(root.val, self.i)
    if self.i == self.cnt - 1:
        self.res = root.val
    self.i += 1
    
    self.dfs(root.right)