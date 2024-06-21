from typing import List


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

class Solution2():
  def nqueens(self, n):
    """
    input: int n
    return: int[][]
    """
    # write your solution here
    self.res = 0
    self.dfs(0, n, [])
    return self.res            
  
  def dfs(self, i, n, path):
    # base case
    if i == n:
      print(path)
      self.res += 1
      return
    # print(path)
    # recursive rule
    for j in range(n):
      if self.check(path, j):
        path.append(j)
        self.dfs(i + 1, n, path)
        path.pop()

  def check(self, path, j):
    row = len(path)
    for i in range(len(path)):
      # check dia
      if abs(i - row) == abs(path[i] - j):
        return False
      
      # check column
      if path[i] == j:
        return False
    
    # print(path, j)
    return True


sol = Solution2()
res = sol.nqueens(4)
print(res)