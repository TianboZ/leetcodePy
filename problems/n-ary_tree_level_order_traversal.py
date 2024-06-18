from collections import deque
from typing import List


class Solution:
  def levelOrder(self, root: 'Node') -> List[List[int]]:
    if not root:
      return root
    
    queue = deque([])
    queue.append(root)
    res = []

    while queue:
      size = len(queue)
      nodes = []
      for i in range(size):
        curr = queue.popleft()
        nodes.append(curr.val)

        for nei in curr.children:
          queue.append(nei)

      res.append(nodes)
    return res
