"""
contains duplicate

[1, 2, 1, 1, 3]

"""
class Solution(object):
  def permutations(self, input):
    """
    input: string input
    return: string[]
    """
    # write your solution here
    if not input: 
      return ['']
    self.res = []
    arr = list(input)
    self.dfs(list(input), 0)
    return self.res

  def dfs(self, arr, i):
    # base case
    if i == len(arr):
      print(''.join(arr))
      self.res.append(''.join(arr))
      return

    # recursive rule
    visit = set()
    for j in range(i, len(arr)):
      if arr[j] in visit:
        continue

      visit.add(arr[j])
      self.swap(arr, i, j)
      self.dfs(arr, i + 1)
      self.swap(arr, i, j)

  def swap(self, arr, i, j):
    arr[i], arr[j] =  arr[j] ,  arr[i] 


sol = Solution()
sol.permutations('1123')