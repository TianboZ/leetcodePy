from typing import Optional
from UtilityClasses import *

class Solution:
  def searchBST(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root: return None
    
    if root.val == key: return root
    
    if root.val > key: 
      return self.searchBST(root.left, key)
    else:
      return self.searchBST(root.right, key)