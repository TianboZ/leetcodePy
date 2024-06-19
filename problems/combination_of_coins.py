class Solution(object):
  def combinations(self, target, coins):
    """
    input: int target, int[] coins
    return: int[][]
    """
    # write your solution here
    self.res = []
    self.dfs(0, 0, target, coins, [])
    print(self.res)
    return self.res

  def dfs(self, sum, i, target, coins, list):
    #  base case
    if i == len(coins):
      if sum == target:
        tmpt = list[:] # copy list
        self.res.append(tmpt)
      return

    #  recursive rule
    coin = coins[i]
    j = 0
    while j * coin + sum <= target:
      list.append(j)
      self.dfs(sum + j * coin, i + 1, target, coins, list)
      list.pop()
      j += 1

class Soluiton2:
  def combinations(self, target, coins):
    """
    input: int target, int[] coins
    return: int[][]
    """
    # write your solution here
    self.res = []
    self.dfs(coins, target, 0, 0, [])
    print(self.res)
    return self.res
  
  def dfs(self, coins, target, sum, i, path):
    # base case
    if i == len(coins):
      print('111')
      if sum == target:
        self.res.append(path.copy())
      return

    # recursive rule
    c = coins[i]
    cnt = 0
    while sum + cnt * c  <= target:
      currSum = sum + cnt * c
      print('currSum', currSum, 'cnt', cnt)
      path.append(cnt)
      self.dfs(coins, target, currSum, i + 1, path)
      path.pop()
      cnt += 1

sol = Soluiton2()
sol.combinations(10, [25, 10, 5, 1])
    


