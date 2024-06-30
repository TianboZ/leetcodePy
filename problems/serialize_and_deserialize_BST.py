# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from UtilityClasses import TreeNode


class Codec:

  def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    nodes = []
    def dfs(root):
      if not root:
        return
      nodes.append(str(root.val))
      dfs(root.left)
      dfs(root.right)
    
    dfs(root)
    return ','.join(nodes)
      

  def deserialize(self, data):
    """Decodes your encoded data to tree.
    :type data: str
    :rtype: TreeNode
    """
    nodes = data.split(',')
    print(nodes)
    self.i = 0 # preorder index

    # lo is BST lower bound, hi is BST higher bound value
    def dfs(lo, hi):
      # base case
      if self.i == len(nodes):
        return None

      # recursive rule
      print(nodes[self.i])
      val = int(nodes[self.i])
      if val <= lo or val >= hi: 
        return None
      
      root = TreeNode(val)
      self.i += 1
      root.left = dfs(lo, val)
      root.right = dfs(val, hi)

      return root  
    
    return dfs(-10000, 10000)
  

sol = Codec()
node2 = TreeNode(2)
node3 = TreeNode(3)
node1 = TreeNode(1)
node4 = TreeNode(11)

node2.left = node1
node2.right = node3
node3.right = node4

data = sol.serialize(node2)
print(data)

root = sol.deserialize(data)
print(root)