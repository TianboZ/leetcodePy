"""
leaf to leaf path

"""

from UtilityClasses import TreeNode


class Solution(object):
  def maxPathSum(self, root: TreeNode):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    self.globalmax = -1000
    self.getMax(root)
    return self.globalmax
  
  # find the max path sum from root to leaf
  def getMax(self, root)->int:
    # base case
    if not root:
      return 0

    # recursive rule
    left = self.getMax(root.left)
    right = self.getMax(root.right)
    if root.left and root.right:
      localmax = left + root.val + right
      self.globalmax = max(self.globalmax, localmax)

      pathmax = max(root.val + left, root.val + right)
      return pathmax
    
    if root.left:
      return root.val + left
    if root.right:
      return root.val + right
    return root.val



sol = Solution()
n1 = TreeNode(-1)
n2 = TreeNode(2)
n3 = TreeNode(11)
n4 = TreeNode(6)
n5 = TreeNode(-14)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

res = sol.maxPathSum(n1)
print(res)

