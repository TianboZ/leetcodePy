class Solution(object):
  def isBalanced(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    res = self.helper(root)
    return res >= 0
      
  # return tree height. if tree is not balanced, return -1
  def helper(self, root):
    if not root: return 0
    
    left = self.helper(root.left)
    right = self.helper(root.right)
    
    if left == -1 or right == -1: return -1
    
    if abs(left - right) >= 2: return -1
    
    return max(left, right) + 1
    
      