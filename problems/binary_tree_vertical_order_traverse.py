# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
solution:
- preorder traverse tree
- use map to record, key: col, value: [[level, value], [] ]


complexity:
time O(n)
space O(n)

"""

from typing import List


class Solution(object):
  def verticalOrder(self, root):
    """
    input: TreeNode root
    return: Integer[]
    """
    # write your solution here
    # sanity check
    if not root:
      return []
      
    map = {}
    self.min = 0
    self.max = 0
    self.dfs(root, map, 0, 0)
    print(map)
    res = []
    
    # build answer
    for i in range(self.min, self.max + 1):
      values = map.get(i)
      values.sort()
      for v in values:
        res.append(v[1])

    return res


  def dfs(self, root, map, col, level):
    if not root:
      return
    
    # get column range
    self.min = min(self.min, col)
    self.max = max(self.max, col)
    
    if col not in map:
      map[col] = []
    map.get(col).append([level, root.val])

    self.dfs(root.left, map, col - 1, level + 1)
    self.dfs(root.right, map, col + 1, level + 1)
