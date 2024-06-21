class Solution(object):
  def numNodesLeft(self, root):
    """
    :type root: TreeNode
    """
    self.dfs(root)
    return root
  
  def dfs(self, root):
    if not root: 
      return 0

    left = self.dfs(root.left)
    right = self.dfs(root.right)
    root.numNodesLeft = left
    return left + right + 1