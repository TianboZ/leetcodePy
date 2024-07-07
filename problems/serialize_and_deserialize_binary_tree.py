"""
soluiton:
      1
    /  \
   2     3
  /\    /   \
 #  #   #    4 
            / \
           #   #  
               

null node use # prepresent
preorder serialize: [1, 2, #, #, 3, #, 4, #, #]  

"""


class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Codec:
  def serialize(self, root)->str:
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    nodes = []

    def dfs(root):
      if not root:
        nodes.append('')
        return 

      nodes.append(str(root.val))
      dfs(root.left)
      dfs(root.right)

    dfs(root)
    print(nodes)
    return ','.join(nodes)
    

  def deserialize(self, data:str):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """

    nodes = data.split(',')
    print(nodes)
    
    self.i = 0 # preorder index
    
    # iterate nodes, build tree recursively
    def dfs()->TreeNode | None:
      # base case
      if self.i == len(nodes):
        return None
      
      if not nodes[self.i]:
        # empty node
        self.i += 1
        return None

      # recursive rule
      root = TreeNode(int(nodes[self.i]))
      self.i += 1
      root.left = dfs()
      root.right = dfs()
      return root

    return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


sol = Codec()
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node.left = node2
node.right = node3
node3.left = node4
node4.right = node5

"""
      1
    /  \
   2   3
      /
     4
     \
       5  

serialize: [1, 2, '', '', 3, 4, '', 5, '', '', '']      
"""

s = sol.serialize(node)
sol.deserialize(s)