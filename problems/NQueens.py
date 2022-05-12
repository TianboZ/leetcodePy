class Solution(object):
  def nqueens(self, n):
    """
    input: int n
    return: int[][]
    """
    # write your solution here
    self.res = []
    self.dfs([], n, 0)  
    return self.res
          
  def dfs(self, list, n, i):
    # base case
    if n == i:
      tmpt = list[:] # copy
      self.res.append(tmpt)  
      return
    
    # recursive rule
    for j in range(n):
      if self.valid(list, j, i):
        list.append(j)
        self.dfs(list, n, i + 1)
        list.pop()
  
  def valid(self, list, col, row):
    for row2 in range(len(list)):
      col2 = list[row2]
      if abs(row - row2) == abs(col - col2): return False
      if col == col2: return False
    
    return True
            

sol = Solution()
res = sol.nqueens(4)
print(res)