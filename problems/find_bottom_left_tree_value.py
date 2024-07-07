class Solution:
  def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    self.maxlevel = -1    
    self.res = 0
    self.dfs(root, 0)

    return self.res
  
  def dfs(self, root, level):
    if not root:
      return

    if level > self.maxlevel:
      self.res = root.val
      self.maxlevel = level
    
    self.dfs(root.left, level + 1)
    self.dfs(root.right, level + 1)