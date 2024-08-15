"""
player 1: x
player 2: 0

player 1 first move

assume each move is valid

complexity:

move(): 
time: o(x)   x is cnt 

total:
space o(m * n), board

"""

class Game:
  
  def __init__(self, m, n, cnt):
    self.grid = [[ None for _ in range(n)] for _ in range(m)]  # m x n board 
    self.map = {
      1: 'x',
      2: '0'
    }
    self.winCnt = cnt

  # return 1 if 1 wins, return 2 if 2 wins, return 0 if tie
  def move(self, player, i, j)->int:
    # directions, up, down, diagnoal 
    dirs = [ [[0, 1], [0, -1]], [ [1, 0], [-1, 0] ],   [ [-1, -1], [1, 1]] ,  [ [-1, 1], [1, -1] ]     ]   
    mark = self.map[player]
    self.grid[i][j] = mark

    for pair in dirs:
      cnt = 1
      for dir in pair: 
        dx, dy = dir  # e.g. [0, 1]
        # print(dir, dx, dy)
        x2 = i + dx
        y2 = j + dy

        while self.isValid(x2, y2) and self.grid[x2][y2] == mark:
          cnt += 1
          x2 += dx
          y2 += dy
      if cnt >= self.winCnt:
        return player
      
    return 0


      

  # check if x,y is in bound
  def isValid(self, x, y)->bool:
    return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])

# test
game  =Game(3, 3, 3)

print(game.move(1, 0, 0))
print(game.move(2, 0, 1))
print(game.move(1, 1, 1))
print(game.move(2, 1, 2))
print(game.move(1, 2, 2)) #  player 1 wins, return 1

