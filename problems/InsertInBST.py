from UtilClass import *

def insert(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    # write your solution here
    if not root: return TreeNode(key)

    if root.val < key:
      root.right = self.insert(root.right, key)
    elif root.val > key:
      root.left = self.insert(root.left, key)
    
    return root
