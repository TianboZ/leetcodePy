from UtilityClasses import *

class Solution(object):
  def insert(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    # write your solution here
    #  base case
    if not root:
      return TreeNode(key)
    
    # recursive rule
    if root.val == key: return root

    if root.val < key:
      root.right = self.insert(root.right, key)
    else:
      root.left = self.insert(root.left, key)

    return root

