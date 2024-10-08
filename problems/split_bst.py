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
      roots = self.splitBST(root.left, target)
      root.left = roots[1]
      return [roots[0], root]
    else:
      roots = self.splitBST(root.right, target)
      root.right = roots[0]
      return [root, roots[1]]