from typing import Optional, List
from UtilityClasses import TreeNode

"""
solution:
- for each tree node, get it's serialization representation. count its frequency

      1
      /\
     2  3
         \
         4
serialize string: " 1,2,#,#,3,#,4,#,# "

very slow

solution 2:
optimization:
traverse the tree and build serialized tree


"""

class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    self.map = {}
    self.res = []
    self.dfs(root)
    return self.res
  
  # traverse tree, return serialized subtree
  def dfs(self, root)->str:
    if not root:
      return '#'

    left = self.dfs(root.left)
    right = self.dfs(root.right)
    tree = ','.join([str(root.val), left, right])

    self.map[tree] = self.map.get(tree, 0) + 1
    if self.map[tree] == 2:
      self.res.append(root)

    return tree
  
class Solution2:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    self.map = {}
    self.res = []
    self.traverse(root) 
    return self.res
  
  # traverse tree
  def traverse(self, root):
    if not root:
      return
    
    path = []
    self.serialize(root, path)
    path = ','.join(path)
    self.map[path] = self.map.get(path, 0) + 1
    if self.map.get(path) == 2:
      self.res.append(root)

    self.traverse(root.left)
    self.traverse(root.right)

  # serialize tree
  def serialize(self, root, path):
    if not root:
      path.append('')
      return 
    path.append(str(root.val))
    self.serialize(root.left, path)
    self.serialize(root.right, path)