from asyncio.windows_utils import BUFSIZE
import collections
from typing import *
from UtilClass import *

# sol1: BFS  sol2: DFS


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = collections.deque([])
        # initial
        queue.append(root)

        # terminale
        while queue:
            tmp = []
            size = len(queue)
            for i in range(size):
                # expand
                node = queue.popleft()
                tmp.append(node.val)
                # generate
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
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
