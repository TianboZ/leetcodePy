class Solution:
  def exist(self, root, target):
    prefixSums = set()
    return self.dfs(root, prefixSums, 0, target)
  def dfs(self, root, prefixSums: set, prefixSum, target):
    # base case
    if not root:
      return False
    # recursive rule
    sum = prefixSum + root.val
    prefixSums.add(sum)
    if sum - target in prefixSums:
      return True
    left = self.dfs(root.left, prefixSums, sum, target)
    right = self.dfs(root.right, prefixSums, sum, target)
    return left or right

