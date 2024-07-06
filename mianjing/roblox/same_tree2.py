

from collections import deque

class Node:
  def __init__(self, val: str, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    

class TreeIterator:
  def __init__(self, node: Node):
    self.stack  = deque([node])
    self.currentLeaf = None
    self.i = 0
  
  def hasNext(self)->bool:
    return self.stack
  
  # find next node
  def next(self) -> Node:
    top = self.stack.pop()
    if top.right:
      self.stack.append(top.right)  
    if top.left:
      self.stack.append(top.left)  

    return top
  
  # find next leaf
  def nextLeaf(self)-> Node | None:
    while self.hasNext():
      next = self.next()
      if not next.left and not next.right:
        self.currentLeaf = next
        print('[nextLeaf], currentLeaf ', self.currentLeaf.val)
        return next
    
    self.currentLeaf = None
    return None

  # O(1)
  def nextChar(self):
    c = None
    if self.currentLeaf:
      c = self.currentLeaf.val[self.i]
      print(c)
      self.i += 1
      if self.i == len(self.currentLeaf.val):
        # should find next leaf leaf, reset current leaf
        self.i = 0
        self.currentLeaf = None

      return c  

    return c

class Solution:
  def sameTree(self, n1, n2):
    it = TreeIterator(n1)
    it2 = TreeIterator(n2)
    
    while (it.currentLeaf or  it.nextLeaf()) and (it2.currentLeaf or  it2.nextLeaf()):
      c = it.nextChar()
      c2 = it2.nextChar()
      if c != c2:
        return False
    
    return (not it.currentLeaf and not it.nextLeaf()) and (not it2.currentLeaf and not it2.nextLeaf())


n1 = Node('a')
n2 = Node('bc')
n3 = Node('de')
n4 = Node('gf')
n5 = Node('123')

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
"""
      a
     / \ 
    bc  de
        /   \
       gf   123

"""



n11 = Node('a1')
n22 = Node('b')
n33 = Node('de')
n44 = Node('cgf')
n55 = Node('123')

n11.left = n22
n11.right = n33
n33.left = n44
n33.right = n55
"""
      a1
     / \ 
    b  de
        /   \
       cgf   123

"""



sol = Solution()
res = sol.sameTree(n1, n11)

print(res)
