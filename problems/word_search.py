"""
solution:
1. for each char in grid, if it match 1st letter or word
2. run DFS

complexity:
N: word length

time
O(N * branch ^ level) = O(N * 4^N) 
space
O(N)

"""

from typing import List


DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    self.res = False
    m = len(board)
    n = len(board[0])
    visit = [[False for _ in range(n)] for _ in range(m)]

    for i in range(m):
      for j in range(n):
        if board[i][j] == word[0]:
          self.dfs(board, i, j, visit, 0, word)

    return self.res

  def dfs(self, grid, i, j, visit, level, word):
    # base case
    if self.res:
      return
    # recursive rule
    if level == len(word) - 1:
      self.res = True
      return
    visit[i][j] = True
    for dx, dy in DIR:
      i2 = dx + i
      j2 = dy + j
      if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]) and not visit[i2][j2]:
        # 在这里做校验更好，因为和最外面call dfs的时候语义一致，都是下一条合法，才继续
        if grid[i2][j2] == word[level + 1]:
          self.dfs(grid, i2, j2, visit, level + 1, word)
      
    visit[i][j] = False
        
        


sol  = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
res = sol.exist(board, "SEE")
print(res)