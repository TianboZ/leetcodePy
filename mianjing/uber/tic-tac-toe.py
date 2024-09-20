"""
1: x
2: o
"""


class TicTacToe:

  def __init__(self, n: int):
    self.grid = [[None for _ in range(n)] for _ in range(n)]
    self.map = {1: 'x', 2: 'o'}
    self.n = n
        
  def move(self, row: int, col: int, player: int) -> int:
    mark = self.map.get(player)
    dirs = [ [[1, 0], [-1, 0]],  [[0, 1], [0, -1]],  [[-1, -1], [1, 1]],   [[-1, 1], [1, -1]]]
    self.grid[row][col] = self.map.get(player)

    for pair in dirs:
      cnt = 1
      # print(pair, pair[0])
      for dir in pair:
        dx, dy = dir
        x2 = row + dx 
        y2 = col + dy
        while self.isValid(x2, y2) and self.grid[x2][y2] == mark:
          cnt += 1
          x2 = x2 + dx 
          y2 = y2 + dy
      if cnt >= self.n:
        return player
    return 0

  def isValid(self, x, y):
    return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)