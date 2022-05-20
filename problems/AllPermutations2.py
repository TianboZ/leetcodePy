from typing import Set, List


class Solution(object):
  def permutations(self, input):
    """
    input: string input
    return: string[]
    """
    # write your solution here
    self.res = []
    self.dfs(list(input), 0)
    return self.res

  def dfs(self, arr: List[int], i):
    #  base case
    if i == len(arr):
      self.res.append(''.join(arr))
      return

    # recursive rule
    print(1)
    set: Set = {'1'}
    j = i
    while j < len(arr):
      if arr[j] not in set:
        set.add(arr[j])
        self.swap(arr, i, j)
        self.dfs(arr, j + 1)
        self.swap(arr, i, j)
      print(j)
      j += 1


  def swap(self, arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

sol = Solution()
res = sol.permutations('abbc')
print(res)