class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.ans = []
    self.dfs(0, nums, 0, n, k, [])
    return self.ans

  def dfs(self, i, nums, currSum, target, count, path):
    # base case
    if (len(path) == count):
      if currSum == target:
        print(path)
        self.ans.append(list(path))

      return

    if i == len(nums):
      return

    # recursive rule
    n = nums[i]

    # case 1: use n
    if currSum + n <= target:
      path.append(n)
      self.dfs(i + 1, nums, currSum + n, target, count, path)
      path.pop()

    # case 2: not use n
    self.dfs(i + 1, nums, currSum, target, count, path)
