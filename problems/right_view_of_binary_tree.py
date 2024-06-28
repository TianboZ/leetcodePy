from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def rightView(self, root):
    """
    input: TreeNode root
    return: Integer[]
    """
    # write your solution here
    res = []
    if not root: return res

    # initial
    q = deque([])
    q.append(root)

    # terminate
    while q:
      size = len(q)
      for i in range(size):
        # expand
        node = q.popleft()
        if i == size - 1:
          res.append(node.val)

        # generate
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
    return res    
  

class Solution2(object):
  def rightView(self, root):
    self.res = []
    map = {}  # key: level    value: right view treenode's val
    self.dfs(root, 0, map)
    return self.res
  
  def dfs(self, root, level, map):
    if not root:
      return
    
    if level not in map:
      map[level] = root.val
      self.res.append(root.val)
    
    self.dfs(root.right, level + 1, map)
    self.dfs(root.left, level + 1, map)