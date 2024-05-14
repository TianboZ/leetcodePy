from typing import List
from collections import deque
from copy import deepcopy

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
wall = -1
empty = 2147483647
gate = 0

class Solution:
  def wallsAndGates(self, rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    m = len(rooms)
    n = len(rooms[0])
    q = deque([])

    for i  in range(m):
      for j in range(n):
        if rooms[i][j] == gate:
          q.append((i, j))

    dis = 0
    while q:
      size = len(q)
      for i in range(size):
        # expand
        curr = q.popleft()
        (row, col) = curr
        rooms[row][col] = dis

        # generate
        for d in dir:
          (x, y) = d
          x = row + x
          y = col + y
          if (x >= 0 and x < m and y >= 0 and y < n):
            if rooms[x][y] == empty:
              q.append((x, y))
              rooms[x][y] = dis + 1

      dis += 1

  # method 2, use visis array
  def wallsAndGates2(self, rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """

    m = len(rooms)
    n = len(rooms[0])

    q = deque([])
    visit = deepcopy(rooms)

    for i  in range(m):
      for j in range(n):
        visit[i][j] = False
        if rooms[i][j] == gate:
          q.append((i, j))
          visit[i][j] = True

    dis = 0
    while q:
      size = len(q)
      for i in range(size):
        # expand
        curr = q.popleft()
        (row, col) = curr
        rooms[row][col] = dis

        # generate
        for d in dir:
          (x, y) = d
          x = row + x
          y = col + y
          if (x >= 0 and x < len(rooms) and y >= 0 and y < len(rooms[0])):
            if not visit[x][y] and rooms[x][y] == empty:
              q.append((x, y))
              visit[x][y] = True

      dis += 1


# test
sol = Solution()
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
sol.wallsAndGates(rooms)
for row in rooms:
  print(row)


