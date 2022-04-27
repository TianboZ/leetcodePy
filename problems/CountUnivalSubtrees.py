class Solution:
    res = 0
    def countUnivalSubtrees(self, root) -> int:
      self.helper(root)
      return self.res
      
    # return true if tree is same value
    def helper(self, root) -> bool:
      if not root: return True
      
      left = self.helper(root.left)
      right = self.helper(root.right)
      
      if left and right and (not root.left or root.left.val == root.val) and \
      (not root.right or root.right.val == root.val):
        self.res += 1
        return True
      
      return False

print(1)