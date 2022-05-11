class Solution(object):
  def subSets(self, set):
    """
    input : String set
    return : String[]
    """
    # write your solution here
    self.res = []
    self.dfs(set, 0, [])
    return self.res

  def dfs(self, str, i, list):
    # base case
    if i == len(str):
      self.res.append(''.join(list))
      return
    
    # recursive rule
    # case1: add str[i]
    list.append(str[i])
    self.dfs(str, i + 1, list)
    list.pop()

    # case2: not add str[i]
    self.dfs(str, i + 1, list)


sol = Solution()
res = sol.subSets('abc')
print(res)

