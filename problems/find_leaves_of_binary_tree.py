# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import collections
from problems.UtilityClasses import TreeNode

"""
solution1
remove leaves recusively, until no leaves left

time O(n^2)

solution2
use map to record each node height, key is height, value is array of nodes
    1
    / \
   2   3
  /  \   
 4    5 

map {
  0: [4, 5, 3],
  1: [2],
  2: [1]
}


complexity:

time O(n)
space O(n)

"""
class Solution:
  def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    while root:
      nodes = []
      root = self.dfs(root, nodes)
      res.append(nodes)
    return res
  
  # remove leaves, and add leaves into `nodes`, return root of trimmed tree
  def dfs(self,root, nodes):
    if not root:
      return root

    if not root.left and not root.right:
      # leave
      nodes.append(root.val)
      root = None
      return None
    
    root.left = self.dfs(root.left, nodes)
    root.right = self.dfs(root.right, nodes)
    return root
  

class Solution2:
  def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
    map = collections.defaultdict(list)
    maxheight = self.dfs(root, map)
    
    # build answers
    res = []
    print(map)
    for h in range(1, maxheight + 1):
      res.append(map[h])

    return res


  # return height of the root
  def dfs(self, root, map)->int:
    if not root:
      return 0
    
    left = self.dfs(root.left, map)
    right = self.dfs(root.right, map)

    height = max(left, right) + 1
    map[height].append(root.val)
    
    return height