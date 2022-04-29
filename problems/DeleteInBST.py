
class Solution(object):
  def deleteTree(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    # write your solution here
    if not root: return root

    if root.val == key:
      if not root.left and not root.right: return None
      if not root.left and root.right: return root.right
      if not root.right and root.left: return root.left

      # find root's successor
      node = self.successor(root.right)
      root.val = node.val
      root.right = self.deleteTree(root.right, node.val)

    elif key < root.val:
      root.left = self.deleteTree(root.left, key)
    else:
      root.right = self.deleteTree(root.right, key)
    
    return root

  def successor(self, root):
    node = root
    while root.left:
      root = root.left
    
    if root: return root
    return node