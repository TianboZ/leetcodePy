class Solution(object):
  def validParentheses(self, n):
    """
    input: int n
    return: string[]
    """
    # write your solution here

    self.res = []
    self.dfs(0, 0, 0, [], n)
    return self.res
  

  # left: # of (    
  # right: # of )
  # path: record path info, e.g [(, (, ...]
  def dfs(self, left, right, i, path, n):
    # base case
    if i == 2 * n:
      if len(path) == 2 * n:
        self.res.append(''.join(path))
      return

    # recursive rule
    # attempt add (
    if left < n:
      path.append('(')
      self.dfs(left + 1, right, i + 1, path, n)
      path.pop()
    
    # attempt add )
    if right < n and left > right:
      path.append(')')
      self.dfs(left, right + 1, i + 1, path, n)
      path.pop()


sol = Solution()
res = sol.validParentheses(2)
print(res)