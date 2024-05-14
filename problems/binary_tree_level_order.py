from collections import deque
from typing import *
from UtilityClasses import *

# sol1: BFS  sol2: DFS

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    if not root:
        return res

    q = deque([])
    # initial
    q.append(root)

    # terminale
    while q:
      tmp = []
      size = len(q)
      for i in range(size):
        # expand
        node = q.popleft()
        tmp.append(node.val)
        # generate
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      res.append(tmp)

    return res


class Solution2:
    # dfs
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        if not root:
            return self.res

        self.dfs(root, 0)
        return self.res

    def dfs(self, root, level):
        if not root:
            return

        if level >= len(self.res):
            self.res.append([])
        self.res[level].append(root.val)

        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
