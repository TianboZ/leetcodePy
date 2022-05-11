class Solution(object):
  def validParentheses(self, n):
    """
    input: int n
    return: string[]
    """
    # write your solution here
    self.res = []
    self.dfs([], 0, 0, 2 * n)

    print(self.res)
    return self.res
  
  # left: # of (,  
  def dfs(self, list, left, right, n):
    #  base case
    if left + right == n:
      if left == right:
        tmp = ''.join(list)
        self.res.append(tmp)
      
      return

    # recursive rule
    # case1: add (
    if left >= right:
      list.append('(')
      self.dfs( list, left + 1, right, n)
      list.pop()

    # case2: add )
    if right < left:
      list.append(')')
      self.dfs( list, left, right + 1, n)
      list.pop()



sol = Solution()
sol.validParentheses(3)