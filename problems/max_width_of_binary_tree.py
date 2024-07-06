# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
soluiton:
index nodes on same level
      0
    /   \   
    0    1
   /\    /\
  0  1   2 3
     /\  \
     2 3  5

parent col: n
parent.left: 2n, parent.right: 2n + 1

map: <dfs level, node's column index> 

"""


class Solution:
  def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.map = {}
    self.res = 1
    self.dfs(root, 0, 0)
    return self.res

  def dfs(self, root, level, col):
    if not root:
        return

    if level not in self.map:
      self.map[level] = col

    if col != self.map.get(level):
      localMax = col - self.map.get(level) + 1
      self.res = max(self.res, localMax)

    self.dfs(root.left, level + 1, col * 2)
    self.dfs(root.right, level + 1, col * 2 + 1)
