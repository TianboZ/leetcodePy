"""
root-to-leaf path sum == target

"""
class Solution(object):
  def exist(self, root, target):
    """
    input: TreeNode root, int target
    return: boolean
    """
    # write your solution here
    self.res = False
    self.dfs(root, 0, target)
    return self.res
  
  def dfs(self, root, sum, target):
    if self.res:
      return 
    if not root:
      return 
    
    if not root.left and not root.right:
      # leaf
      if sum + root.val == target:
        self.res = True

    self.dfs(root.left, sum + root.val, target)
    self.dfs(root.right, sum + root.val, target)