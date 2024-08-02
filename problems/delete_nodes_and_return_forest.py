# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
complexity:
time O(n)
space O(n)
"""

class Solution:
  def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    roots = set(to_delete)
    # print(roots)
    self.res = []
    root = self.dfs(root, roots)
    # print(r.val)
    if root:
      self.res.append(root)
    return self.res
    
  # return root after delete some nodes
  def dfs(self, root, roots) -> TreeNode:
    if not root:
      return None
    
    left = self.dfs(root.left, roots)
    right = self.dfs(root.right, roots)
    
    root.left = left
    root.right = right

    if root.val in roots: 
      if left:
        self.res.append(left)
      if right:
        self.res.append(right)
    
      return None
    else:
      return root
    

        