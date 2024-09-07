
from typing import List


class Solution:
  def diffWaysToCompute(self, expression: str) -> List[int]:
    res=self.dfs(expression)
    # print(res)
    # return []
    return res
  
  def dfs(self, exp)->List[int]:
    # baes case
    if not exp:
      return []
    
    # recursive rule
    res = []
    for i in range(len(exp)):
      c = exp[i]
      
      # when it is operand, start divide and concour 
      if c == '+' or c == '-' or c == '*':
        left = self.dfs(exp[0:i])
        right = self.dfs(exp[i + 1: len(exp)])
        for l in left:
          for r in right:
            if c == '+':
              res.append(l + r)
            elif c == '-':
              res.append(l - r)
            else:
              # *
              res.append(l * r)
    
    if not res:
      # exp is number, e.g. 33
      return [int(exp)]
    
    return res