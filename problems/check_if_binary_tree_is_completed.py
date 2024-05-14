'''
新的思想，可以把null node加到queue里

'''

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    empty_flag = False

    q = deque([])
    q.append(root)
    while q:
      curr = q.popleft()
      
      if not curr:
        empty_flag = True
      else:
        if empty_flag:
          return False

      if curr:
        q.append(curr.left)
        q.append(curr.right)

    return True    