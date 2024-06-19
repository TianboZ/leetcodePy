class Solution(object):
  def subSets(self, set):
    """
    input : String set
    return : String[]
    """
    # write your solution here
    ans = []
    self.dfs(set, 0, [], ans)
    return ans

  def dfs(self, str: str, i, path: list, res):
    # base case
    if i == len(str):
      res.append(''.join(path))
      return

    # recursive rule
    c = str[i]

    # branch 1
    path.append(c)
    self.dfs(str, i + 1, path, res)
    path.pop()

    # branch 2
    self.dfs(str, i + 1, path, res)


sol = Solution()
res = sol.subSets('abc')
print(res)

