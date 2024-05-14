class Solution(object):
  def findHeight(self, root):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    if not root: return 0

    return max(self.findHeight(root.left),self.findHeight(root.right)) + 1

