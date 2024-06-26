"""
any node to any node, downwards only

"""
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
    
    if sum == target:
      return True

    if sum - target in prefixSums:
      return True
    
    added = False
    if sum not in prefixSums:
      added = True
      prefixSums.add(sum)

    left = self.dfs(root.left, prefixSums, sum, target)
    right = self.dfs(root.right, prefixSums, sum, target)

    if added:
      prefixSums.discard(sum)
    return left or right
