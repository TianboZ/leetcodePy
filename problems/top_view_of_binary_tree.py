# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""

solution:
- DFS preorder tree
- use map record <column, first appear node on this column>

compleixty:
time o(n)
space o(n)

"""

class Solution(object):
  def topView(self, root):
    """
    input: TreeNode root
    return: Integer[]
    """
    # write your solution here
    if not root:
      return []
    
    map = {}
    self.range = [0, 0]
    self.dfs(root, 0, 0, map)
    res = []
    
    # build answer
    for i in range(self.range[0], self.range[1] + 1):
      res.append(map.get(i)[1])
    return res

  def dfs(self, root, col, level, map):
    if not root:
      return
    
    # record colunm range
    l, r = self.range
    l = min(l, col)
    r = max(r, col)
    self.range = [l, r]

    if col not in map:
      map[col] = [level, root.val]
    else:
      if map.get(col)[0] > level:
        map[col] = [level, root.val]
    
    self.dfs(root.left, col - 1, level + 1, map)
    self.dfs(root.right, col + 1, level + 1, map)