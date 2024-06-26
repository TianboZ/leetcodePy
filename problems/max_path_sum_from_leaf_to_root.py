import math
class Solution(object):
  def maxPathSumLeafToRoot(self, root):
    """
    input: TreeNode root
    return: int
    """
    if not root:
      return -1

    self.res = -math.inf
    self.dfs(root, 0)
    return self.res

  def dfs(self, root, prefixSum):
    if not root:
      return
    
    currSum = prefixSum + root.val
    if not root.left and not root.right:
      self.res = max(self.res, currSum)
    self.dfs(root.left, currSum)
    self.dfs(root.right, currSum)