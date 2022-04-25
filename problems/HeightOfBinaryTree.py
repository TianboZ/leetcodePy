class Solution(object):
  def findHeight(self, root):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    if root is None: return 0
    return 1 + max(self.findHeight(root.left), self.findHeight(root.right))
