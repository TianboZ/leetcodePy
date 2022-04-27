class Solution(object):
  def isSymmetric(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    if not root: return True
    return self.helper(root.left, root.right)

  def helper(self, root, root2):
    if not root and not root2: return True
    if not root or not root2: return False
    if root.val != root2.val: return False

    return self.helper(root.left, root2.right) and self.helper(root.right, root2.left)