"""
solution:
- serialize two tree to string
- compare if s1 is substring of s2

complexity:
time O(m + n)
space O(max(m, n))
"""

class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    path = []
    t1 = self.dfs(root, path)
    path = ','.join(path)

    path2 = []
    t2 = self.dfs(subRoot, path2)
    path2 = ','.join(path2)

    # print(path, path2)
    return path2 in path


  # serialize tree
  def dfs(self, root, path):
    if not root:
      path.append('#')
      return 
    path.append('[' + str(root.val))
    self.dfs(root.left, path)
    self.dfs(root.right, path)