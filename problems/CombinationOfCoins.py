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


sol = Solution()
sol.combinations(10, [25, 10, 5, 1])
    


