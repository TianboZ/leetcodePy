"""
画图！

"""
class Solution:
  def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
    if not root:
      return [None, None]
    
    if root.val == target:
      root2 = root.right
      root.right = None
      return [root, root2]
    
    if root.val > target:
      r1, r2 = self.splitBST(root.left, target)
      root.left = r2
      return [r1, root]
    else:
      r1, r2 = self.splitBST(root.right, target)
      root.right = r1
      return [root, r2]