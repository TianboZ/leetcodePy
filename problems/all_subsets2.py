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
    c = arr[i]

    # branch 1, add arr[i]
    path.append(c)
    self.dfs(arr, i + 1, path)
    path.pop()

    # branch 2, not add arr[i]
    while i + 1 < len(arr) and arr[i] == arr[i + 1]:
      i += 1 # skip all consequtive same value
    self.dfs(arr, i + 1, path)


sol = Solution()
res = sol.subSets('acac')
print(res)

