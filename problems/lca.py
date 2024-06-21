class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    return self.lca(root, p, q)

  def lca(self, root, a, b):
    # base case
    if not root: return None
    if a == root or b == root:
      return root
    
    # recursive rule
    left = self.lca(root.left, a, b)
    right = self.lca(root.right, a, b)
    if left and right:
      return root
    
    if left:
      return left
    
    return right
