class Solution(object):
  def combinations(self, target):
    """
    input: int target
    return: int[][]
    """
    # write your solution here
    factors = []
    self.res = []
    self.getAllFactors(target, factors)
    self.dfs([], target, 0, factors, 1)
    return self.res
  
  def getAllFactors(self, num, factors):
    for i in range(2, num):
      if num % i == 0:
        factors.append(i)

  def dfs(self, path, target, i, factors, prevVal):
    # base case
    
    if prevVal == target:
      # print('path', path, 'factors', factors)
      # generate result
      tmp = []
      for j in range(len(path)):
        factor = factors[j]
        cnt = path[j]
        for _ in range(cnt):
          tmp.append(factor)
      
      self.res.append(tmp)
      return
    
    if i == len(factors):
      return

    # recursive rule
    factor = factors[i]
    cnt = 0
    while prevVal * factor ** cnt <= target:
      path.append(cnt)
      self.dfs(path, target, i + 1, factors, prevVal * factor ** cnt)
      path.pop()
      cnt += 1

sol = Solution()
sol.combinations(24)
