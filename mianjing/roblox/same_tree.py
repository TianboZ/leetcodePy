"""

follow up:
how to end asap? 

assumption1: 不看 中间的nodes, 只看leaves
      1                     2
   /    \                /      \
 hello  world          hell    o  world
          \                        \ 
          x                         x
not same


      1                     2
   /    \                /      \
  hello  world          hell    o  world

same

same question! google onsite
https://leetcode.com/discuss/interview-question/345020/Google-or-Onsite-or-Leaf-Similar-Trees

"""


from collections import deque


class Node:
  def __init__(self, val: str, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class TreeIterator:
  def __init__(self, node: Node):
    self.stack = deque([node])
    self.currleaf = None
    self.i = 0

  def hasNext(self):
    return self.stack

  def next(self)->Node:
    top = self.stack.pop()
    if top.right:
      self.stack.append(top.right)
    
    if top.left:
      self.stack.append(top.left)
    
    return top
  
  def nextLeaf(self)-> Node | None:
    while self.hasNext():
      n = self.next()
      if not n.left and not n.right:
        print('current leaf', n.val)
        self.currleaf = n
        return n
    
    print('current leaf', None)
    self.currleaf = None
    return None
  
  def nextChar(self)->str | None:
    res = None
    if self.currleaf:
      
      print('nextChar(), currentleaf', self.currleaf.val)
      res = self.currleaf.val[self.i]
      print(res)
      self.i += 1
      
      if self.i == len(self.currleaf.val):
        self.currleaf = None
        self.i = 0
      
      return res
    return res

class Solution:
  def drive(self, node: Node, node2: Node):
    it = TreeIterator(node)
    it2 = TreeIterator(node2)
    leaf = []

    while (it.currleaf or it.nextLeaf()) and (it2.currleaf or it2.nextLeaf()):
      c1 = it.nextChar()
      c2 = it2.nextChar()
      if c1 != c2:
        print('not same!')
        return

    finalRes = (not it.currleaf and not it.nextLeaf()) and  (not it2.currleaf and not it2.nextLeaf())
    if finalRes:
      print('same tree')
    else:
      print('not same!')

    # while it.currleaf or it.nextLeaf():
    #   res = it.nextChar()
    #   leaf.append(res)
    # print(leaf)
      


################### drive code
sol = Solution()

"""
        ab
     /      \   
    cd     efg
          /  \
        123  4   
"""

n1 = Node('abxxx')
n2 = Node('cd')
n3 = Node('efg')
n4 = Node('123')
n5 = Node('40')

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5


"""
        ab
     /      \   
    c      defg
          /  \
        d123     4   
"""
n11 = Node('ab')
n22 = Node('c')
n33 = Node('defg')
n44 = Node('d123')
n55 = Node('4')

n11.left = n22
n11.right = n33
n33.left = n44
n33.right = n55

sol.drive(n1, n11)