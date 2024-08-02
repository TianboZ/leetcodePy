# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
solution:
map<int, TreeNode>
child = []
all = []
"""

class Solution:
  def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
    map = {}
    children = set()
    all = set()
    for arr in descriptions:
      p, c, isLeft = arr
      
      all.add(p)
      all.add(c)
      children.add(c)
      
      pNode = None
      if p in map:
        pNode = map[p]
      else:
        pNode = TreeNode(p)
        map[p] = pNode
      
      cNode = None
      if c in map:
        cNode = map[c]
      else:
        cNode = TreeNode(c)
        map[c] = cNode
      
      if isLeft == 1:
        pNode.left = cNode
      else:
        pNode.right = cNode
    
    for v in all:
      if v not in children:
        return map[v]

    return 