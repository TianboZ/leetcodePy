class Solution(object):
  def permutations(self, input):
    """
    input: string input
    return: string[]
    """
    # write your solution here
    res = []
    path = []
    arr = list(input)
    self.dfs(arr, 0, path, res)
    return res

  def dfs(self, arr, i, path, res):
    # basecase
    if i == len(arr):
      res.append(''.join(arr))
      return

    # recursive rule
    for j in range(i, len(arr)):
      self.swap(arr, i, j)
      self.dfs(arr, i + 1, path, res)
      self.swap(arr, i, j)

  def swap(self, arr: list, i, j):
    tmp = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp

sol = Solution()
res = sol.permutations('abc')
print(res)