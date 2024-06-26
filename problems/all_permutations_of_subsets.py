class Solution:
  def allPermutationsOfSubsets(self, set):
    """
    input: string set
    return: string[]
    """
    # write your solution here
    self.res = []
    arr = list(set)
    self.dfs(arr, 0)
    return self.res

  def dfs(self, arr, i):
    # base case
    tmp = arr[0: i]
    print(''.join(tmp))
    self.res.append(''.join(tmp))
    # print('arr', arr)
    if i == len(arr):
      return

    # recursive rule
    j = i
    while j < len(arr):
      self.swap(arr, j, i)
      self.dfs(arr, i + 1)
      self.swap(arr, j, i)
      j += 1

  def swap(self, arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


sol = Solution()
sol.allPermutationsOfSubsets("abc")