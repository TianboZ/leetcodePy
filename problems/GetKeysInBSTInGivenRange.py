class Solution(object):
  def getRange(self, root, min, max):
    """
    input: TreeNode root, int min, int max
    return: Integer[]
    """
    # write your solution here
    res = []
    self.helper(res, root, min, max)
    return res

  def helper(self, res, root, min, max):
    if not root: return

    
    self.helper(res, root.left, min, max)
    if root.val >= min and root.val <= max:
      res.append(root.val)
    self.helper(res, root.right, min, max)