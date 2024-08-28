class Solution(object):
  def subSets(self, set):
    """
    input : String set
    return : String[]
    """
    # write your solution here
    self.res = []
    arr = list(set)
    arr.sort()
    self.dfs(arr, 0, [])
    return self.res

  def dfs(self, arr: list, i, path: list):
    # base case
    if i == len(arr):
      self.res.append(''.join(path))
      return

    # recursive rule
    j = i
    c = arr[j]
    # branch 1, add arr[i]
    path.append(c)
    self.dfs(arr, j + 1, path)
    path.pop()

    # branch 2, not add arr[i]
    # skip all duplicate 
    while j < len(arr) - 1 and arr[j] == arr[j + 1]:
      j += 1

    self.dfs(arr, j + 1, path)

sol = Solution()
res = sol.subSets('acac')
print(res)

