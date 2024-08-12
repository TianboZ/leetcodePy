class Game:
  def __init__(self, m, n, winCnt):
    self.grid = [[ None for _ in range(n)] for _ in range(m)]
    self.winCnt = winCnt
    self.map = {
      1: 'x',
      2: 'o'
    }

  # return 1, player 1 wins; return 2, player 2 wins; return 0 if tie
  def move(self, row, col, player)->int:
    mark = self.map.get(player)
    self.grid[row][col] = mark
    
    # up, down, dignal
    dirs = [ [(1, 0), (-1, 0)], [(0, 1), (0, -1)], [(-1, -1), (1, 1)],  [(1, -1), (-1, 1)] ]

    for pair in dirs:
      cnt = 1
      for dir in pair:
        dx, dy = dir
        x2 = row + dx
        y2 = col + dy
        while self.isValid(x2, y2) and self.grid[x2][y2] == mark:
          cnt += 1
          x2 += dx
          y2 += dy

      if cnt >= self.winCnt:
        return player

    return 0        

  def isValid(self, x, y):
    return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])

