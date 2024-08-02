# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
solution:
- build graph, child -> parent map
- find all leaves
- for each leaf, run DFS, depth is limited to distance
  - if find leaf, then good pair count++

complexity:
time: O(n) + O(leaf_cnt * n) = O(n^2)
space: O(n)

"""
class Solution:
  def countPairs(self, root: TreeNode, distance: int) -> int:
    map = {} # <child, parent>
    leaves = []
    self.cnt = 0
    # build graph, collect all leaf
    self.dfs(root, None, map, leaves)
    
    # print(prev)
    for leaf in leaves:
      visit = set()
      self.dfs2(leaf, 0, visit, distance, map)
      
    print(self.cnt)
    return self.cnt // 2
  
  # traverse
  def dfs(self, root, p, map, leaves):
    if not root:
      return
    if not root.left and not root.right:
      leaves.append(root)

    if p:
      map[root] = p

    self.dfs(root.left, root, map, leaves)
    self.dfs(root.right, root, map, leaves)

  def dfs2(self, root, depth,visit, dis, map):
    if root in visit:
      return
    if not root:
      return
    if depth > dis:
      return 

    visit.add(root)    
    if depth > 0:
      if self.isLeaf(root):
        self.cnt += 1

    self.dfs2(root.left, depth + 1, visit, dis, map)
    self.dfs2(root.right, depth + 1, visit, dis, map)
    self.dfs2(map.get(root), depth + 1, visit, dis, map)
  
  def isLeaf(self, root):
    return not root.left and not root.right