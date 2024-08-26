class Solution:
  def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    return self.dfs(root1, root2)
  
  def dfs(self, root1, root2):
    if not root1 and not root2:
      return None

    if not root2:
      return root1
    
    if not root1:
      return root2
        
    # merge tree2 to tree1
    root1.val += root2.val
    root1.left = self.dfs(root1.left, root2.left)
    root1.right = self.dfs(root1.right, root2.right)

    return root1