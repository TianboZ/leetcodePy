class Solution:
  def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    return self.dfs(root1, root2)
  
  def dfs(self, r1, r2)->bool:
    if not r1 and not r2:
      return True
    if r1 and not r2:
      return False
    if r2 and not r1:  
      return False

    if r1.val != r2.val:
      return False

    return self.dfs(r1.left, r2.left) and self.dfs(r1.right, r2.right) or self.dfs(r1.left, r2.right) and self.dfs(r1.right, r2.left)