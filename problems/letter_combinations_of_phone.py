from typing import List


class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    map = {
      2: ['a', 'b', 'c'],
      3: ['d', 'e', 'f'],
      4: ['g', 'h', 'i'],
      5: ['j', 'k', 'l'],
      6: ['m','n', 'o'],
      7: ['p','q','r','s'],
      8: ['t','u','v'],
      9: ['w','x','y','z']
    }
    self.res = []
    self.dfs(digits, map, 0, [])
    return self.res
  
  def dfs(self, digits: str, map: dict, i, path: list):
    # base case
    if i == len(digits):
      self.res.append(''.join(path))
      print(''.join(path))
      return

    # recursive rule
    num = int(digits[i])
    # print(num)
    for l in map.get(num):
      path.append(l)
      self.dfs(digits, map, i + 1, path)
      path.pop()


sol = Solution()
sol.letterCombinations('23')