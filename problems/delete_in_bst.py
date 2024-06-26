
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
class Solution2:
  def deleteTree(self, root, key):
    # recursive rule
    if not root: return root

    #  recursive rule
    if key > root.val:
      root.right = self.deleteTree(root.right, key)
      return root
    elif key < root.val:
      root.left = self.deleteTree(root.left, key)
      return root
    else:
      if not root.left and not root.right:
        return None
      elif root.left and not root.right:
        return root.left
      elif not root.left and root.right: 
        return root.right
      else:
        su = self.successor2(root.right)
        root.val = su
        root.right = self.deleteTree(root.right, su)
        return root
    return root

  def successor2(self, root):
    val = root.val
    while root:
      val = root.val
      root = root.left
    return val
