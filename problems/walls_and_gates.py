from typing import List
from collections import deque

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
wall = -1
empty = 2147483647
gate = 0

class Solution:
  # method 2, use visit hashset
  def wallsAndGates(self, rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """

    m = len(rooms)
    n = len(rooms[0])

    q = deque([])
    visit = set()

    for i  in range(m):
      for j in range(n):
        if rooms[i][j] == gate:
          q.append((i, j))
          visit.add((i, j))

    dis = 0
    while q:
      size = len(q)
      for i in range(size):
        # expand
        curr = q.popleft()
        row, col = curr
        # update distance from door
        rooms[row][col] = dis

        # generate
        for dr, dc in dirs:
          r2 = row + dr
          c2 = col + dc
          if (0 <= r2  < len(rooms) and 0 <= c2 < len(rooms[0])) and (r2, c2) not in visit and rooms[r2][c2] != -1:
            q.append((r2, c2))
            visit.add((r2, c2))

      dis += 1


# test
sol = Solution()
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
sol.wallsAndGates(rooms)
for row in rooms:
  print(row)


