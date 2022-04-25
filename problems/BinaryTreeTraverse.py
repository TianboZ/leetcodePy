
from typing import *
from UtilClass import *

class Solution:
    res = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      self.helper(root)
      return self.res      
    
    def helper(self, root):
      if root is None: return
      
      self.helper(root.left)
      self.res.append(root.val)
      self.helper(root.right)


sol = Solution()

n = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

"""
      1
      /\
     2  3
        /\
        4 5  
"""

n.left = n2
n.right = n3
n3.left = n4
n3.right = n5


res = sol.inorderTraversal(n)
print('inorder: ', res)

