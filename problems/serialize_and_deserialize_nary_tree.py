"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


https://www.youtube.com/watch?v=QajHKAMc01w&ab_channel=TonyTeaches
solution:
      1
     /\ \ 
    2  3 4
    \
    5

every node has children information with it

preorder serialize: 1#3, 2#1, 5#1, 3#1, 4#1

1#3 meaning: 1 is node value, 3 is child count


"""

class Node(object):
  def __init__(self, val=None, children=[]):
    self.val = val
    self.children = children

class Codec:
  def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: Node
    :rtype: str
    """
    nodes = []

    def dfs(root):
      if not root:
        return
      val = root.val
      childCnt = len(root.children)
      nodes.append(str(val) + "#" + str(childCnt))
      for child in root.children:
        dfs(child)
    
    dfs(root)

    s =  ','.join(nodes)
    print(s)
    return s

  
  
  def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: Node
    """
    if not data:
      return None
    
    nodes = data.split(',')   #    1#3,2#4
    print(nodes)
    self.i = 0 # preorder index
    
    def dfs():
      # base case
      if self.i == len(nodes):
        return None

      # recursive rule
      node = nodes[self.i]
      self.i += 1
      
      pair = node.split('#')
      print(pair)
      val = int(pair[0])
      cnt = int(pair[1])

      root = Node(val)
      neis = []
      for j in range(cnt):
        neis.append(dfs())
      root.children = neis

      return root   
    
    root = dfs()
    return root

# Your Codec object will be instantiated and called as such:
codec = Codec()
node = Node(1)
node2 = Node(2)
node3 =  Node(3)
node4 =  Node(4)
node5 =  Node(5)

node.children = [node2, node3, node4]
node4.children = [node5]
"""
      1
     /\ \ 
    2  3 4
          \
           5


"""
codec.deserialize(codec.serialize(node))


print(int(""))