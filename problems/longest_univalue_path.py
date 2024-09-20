class Solution:
  def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
    self.res = 1
    self.dfs(root)
    return self.res - 1

  # return longest path of same value
  def dfs(self, root)->int:        
    if not root:
      return 0

    left = self.dfs(root.left)
    right = self.dfs(root.right)

    rightPathLen = 1
    leftPathLen = 1
    val = root.val

    if root.right and root.right.val == val:
      rightPathLen += right

    if root.left and root.left.val == val:
      leftPathLen += left

    # find global max
    self.res = max(self.res, rightPathLen, leftPathLen)
    if root.left and root.left.val == val and root.right and root.right.val == val:
      self.res = max(self.res, rightPathLen + leftPathLen - 1)

    # return 
    if rightPathLen > leftPathLen:
      return rightPathLen
    return leftPathLen
  
"""
cleaner solution:
pass target value down to subtree

"""
class Solution2:
  def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
    self.res = 1
    self.dfs(root, None)
    return self.res - 1

  # return longest path of under the root that have same value as root
  def dfs(self, root, parentVal)->int:        
    if not root:
      return 0    
    
    left = self.dfs(root.left, root.val)
    right = self.dfs(root.right, root.val)
    self.res = max(self.res, left + right + 1)

    if root.val != parentVal:
      return 0

    return max(left, right) + 1  