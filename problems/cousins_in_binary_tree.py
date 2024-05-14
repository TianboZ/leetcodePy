# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Cell:
  def __init__(self, prev, level):
    self.prev = prev
    self.level = level

class Solution:
  def isCousins(self, root, x: int, y: int) -> bool:
    map = {}
    self.dfs(root, x, y, map, 0, -1)
    if map.get(x) and map.get(y):
      (prev_x, level_x) = map.get(x)
      (prev_y, level_y) = map.get(y)
      return level_x == level_y and prev_x != prev_y
    return False

  def dfs(self, root, x, y, map, level, prev):
    if not root: return

    if root.val == x:
      map[x] = (prev, level)
    if root.val == y:
      map[y] = (prev, level)
    
    self.dfs(root.left, x, y, map, level + 1, root.val)
    self.dfs(root.right, x, y, map, level + 1, root.val)