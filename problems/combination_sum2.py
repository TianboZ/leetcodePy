class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    path = []
    candidates.sort()
    self.res = []
    self.dfs(candidates, 0, target, 0, path)
    return self.res

  def dfs(self, nums, i, target, sum, path):
    # base case
    if sum == target:
      self.res.append(list(path))
      return
    
    if i == len(nums):
      return

    # recursive rule
    # add nums[i]
    n = nums[i]
    if sum + n <= target:
      path.append(n)
      self.dfs(nums, i + 1, target, sum + n, path)
      path.pop()

    # not add nums[i]
    j = i
    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
      j += 1
    
    self.dfs(nums, j + 1, target, sum, path)