from typing import Optional
from problems.UtilityClasses import TreeNode


class Solution:
  def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    return self.dfs(root)
  # return new root
  def dfs(self, root)->TreeNode:
    if not root or not root.left:
      return root

    newRoot= self.dfs(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None

    return newRoot
        