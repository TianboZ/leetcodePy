"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
from typing import Optional

"""
BFS

time: O(N)
space: O(N)
"""
class Solution:
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    queue = deque([])
    queue.append(root)

    while queue:
      size = len(queue)
      prev = None
      for i in range(size):
        curr = queue.popleft()
        # connect ->
        if i >= 1:
          prev.next = curr
        prev = curr

        if curr.left:
          queue.append(curr.left)
        if curr.right:
          queue.append(curr.right)
    
    return root