# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
any node to any node path

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
  
  # find the max path sum from node
  def getMax(self, node)->int:
    # base case
    if not node:
      return 0

    # recursive rule
    left = self.getMax(node.left)
    right = self.getMax(node.right)

    localMax: int = max(node.val, node.val + left, node.val + right, node.val + left + right)
    self.glabalMax = 100
    self.globalmax = max(self.globalmax, localMax)

    # find a path max sum
    pathMax = node.val
    pathMax = max(pathMax, pathMax + left, pathMax + right)

    return pathMax


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

