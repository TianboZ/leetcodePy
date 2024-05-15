class Solution:
  def fib(self, n: int) -> int:
    memo = {}
    return self.dfs2(n, memo)
    
  def dfs(self, n, memo):
    # base case
    if n == 0: return 0
    if n == 1: return 1


    # recursive rule
    res = memo.get(n - 1, self.dfs(n - 1, memo))
    memo[n - 1] = res
    
    res2 = memo.get(n - 2, self.dfs(n - 2, memo))
    memo[n - 2] = res2

    return res + res2


  def dfs2(self, n, memo):
    if n == 0: return 0
    if n == 1: return 1

    if n in memo: 
      return memo[n]
    
    memo[n] = self.dfs2(n - 1, memo) + self.dfs2(n - 2, memo)
    return memo[n]
  

sol = Solution()
res = sol.fib(100)
print(res)