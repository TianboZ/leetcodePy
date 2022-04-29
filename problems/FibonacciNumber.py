class Solution:
    def fib(self, n: int) -> int:
      self.memo = {}
      return self.dfs(n)
      
    def dfs(self, n):
      if n == 0: return 0
      if n == 1: return 1
      
      if n in self.memo: return self.memo[n]
      self.memo[n] = self.dfs(n - 1) + self.dfs(n - 2)
      return self.memo[n]