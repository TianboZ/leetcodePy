from collections import defaultdict

LEFT = 0
TOP = 1
BOTTOM = 2
RIGHT = 3

def solution(matrix, query):
  m, n = len(matrix), len(matrix[0])
  map = defaultdict(lambda :[None] * 4)

  # top-left traverse
  topBlocker = [-1] * n
  for r in range(m):
    for c in range(n):
      leftBlocker = -1
      if matrix[r][c] == 'X':
        # update blocker pos
        leftBlocker = c
        topBlocker[c] = r
      
      if matrix[r][c] == 'O':
        map[(r,c)][LEFT] = abs(leftBlocker - c)
        map[(r,c)][TOP] = abs(topBlocker[c] - r)


  # bottom-right traverse
  bottomBlocker = [m] * n
  for r in range(m - 1, -1, -1):
    rightBlocker = n
    for c in range(n - 1, -1, -1):
      # print(1)
      if matrix[r][c] == 'X':
        rightBlocker = c
        bottomBlocker[c] = r
      
      if matrix[r][c] == 'O':
        map[(r,c)][BOTTOM] = abs(r - bottomBlocker[c])
        map[(r,c)][RIGHT] = abs(c - rightBlocker)

  print(map)

  # TIME O(m * n)
  for k, v in map.items():
    if v == query:
      print(k)

matrix = [
  ['O','E','E','E','X'],
  ['E','O','X','X','X'],
  ['E','E','E','E','E'],
  ['X','E','O','E','E'],
  ['X','E','X','E','X']
]

query = [2, 2, 4, 1] 

solution(matrix, query)