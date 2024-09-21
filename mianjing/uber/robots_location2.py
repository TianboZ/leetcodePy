
LEFT = 0
TOP = 1
BOTTOM = 2
RIGHT =  3

def solution(grid, query):
  m = len(grid)
  n = len(grid[0])
  map = {} # key: (i, j), value: [left, top, bottom, right]  distance to 4 dirs
  
  # top-left traverse
  topBlocks = [-1] * n
  for i in range(m):
    leftBlock = -1
    for j in range(n):
      if grid[i][j] == 'X':
        # update block pos
        leftBlock = j
        topBlocks[j] = i
      
      if grid[i][j] == 'O':
        left = abs(leftBlock - j)
        top = abs(topBlocks[j] - i)
        
        if (i, j) not in map:
          map[(i, j)] = [0, 0, 0, 0]
        
        map[(i, j)][LEFT] = left 
        map[(i, j)][TOP] = top 
        
  # bottom-right traverse
  bottomBlocks = [m] * n
  for i in range(m - 1, -1, -1):
    rightBlock = n
    for j in range(n - 1, -1, -1):
      if grid[i][j] == 'X':
        # update block pos
        rightBlock = j
        bottomBlocks[j] = i
      
      if grid[i][j] == 'O':
        right = abs(rightBlock - j)
        bottom = abs(bottomBlocks[j] - i)
        
        map[(i, j)][BOTTOM] = bottom
        map[(i, j)][RIGHT] = right
  
  for k, v in map.items():
    print(k, v)
    if v == query:
      print(k)

# test 
matrix = [
  ['O','E','E','E','X'],
  ['E','O','X','X','X'],
  ['E','E','E','E','E'],
  ['X','E','O','E','E'],
  ['X','E','X','E','X']
]

query = [2, 2, 4, 1] # [1,1]

solution(matrix, query)