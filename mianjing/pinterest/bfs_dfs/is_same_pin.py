

from collections import deque


class Pixel:
  def __init__(self, val) -> None:
    self.val  =val
    
def isSamePixel(p1: Pixel, p2: Pixel)->bool:
  return p1.val == p2.val

pins = [
  [Pixel(''), Pixel('1'),Pixel(''),Pixel('') ],
  [Pixel(''), Pixel('1'),Pixel('3'),Pixel('2') ],
  [Pixel(''), Pixel('1'),Pixel('3'),Pixel('2') ],
  [Pixel('3'), Pixel(''),Pixel(''),Pixel('2') ],
]

class Solution:
  def findUniquePins(self, grid: list[list[Pixel]])->int:
    visit = set()
    m = len(grid)
    n = len(grid[0])
    cnt = 0
    for i in range(m):
      for j in range(n):
        p = grid[i][j]
        if not p.val:
          continue
        if (i, j) in visit:
          continue
        self.bfs(grid, i, j, visit)
        cnt += 1
    
    print(cnt)
    print(visit)
    return cnt
    
  def bfs(self, grid, r, c, visit):
    pin = grid[r][c]
    queue = deque([])
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # init
    queue.append([r, c])
    visit.add((r, c))
    
    # terminate
    while queue:
      # expand 
      curr = queue.popleft()
      r1, c1 = curr
      
      # generate
      for dx, dy in dirs:
        r2 = r1 + dx
        c2 = c1 + dy
        if 0<= r2 < len(grid) and 0<= c2 < len(grid[0]) and (r2, c2) not in visit and isSamePixel(pin, grid[r2][c2]):
          visit.add((r2, c2))
          queue.append([r2, c2])
          
# test
sol = Solution()
sol.findUniquePins(pins)