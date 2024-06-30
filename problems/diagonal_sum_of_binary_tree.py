# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def diagonalSum(self, root):
    """
    input: TreeNode root
    return: Integer[]
    """
    # write your solution here
    if not root:
      return []
    
    self.maxlevel = 0
    res = []
    map = {}
    self.dfs(root, map, 0)
    for i in range(0, self.maxlevel + 1):
      res.append(map.get(i))
    return res

  def dfs(self, root, map, level):
    if not root:
      return

    self.maxlevel = max(self.maxlevel, level)
    if level not in map:
      map[level] = 0
    map[level] += root.val
    self.dfs(root.left, map, level + 1)
    self.dfs(root.right, map, level)