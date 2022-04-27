class Solution:
    def maxDepth(self, root) -> int:
      return self.helper(root)
    
    def helper(self, root):
      if not root: return 0
      return max(self.helper(root.left), self.helper(root.right)) + 1
      