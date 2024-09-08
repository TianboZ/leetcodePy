from typing import List
import heapq

'''
solution:
Dijk

time: O(V * logV) -> O( m*n * log(m*n))
space: O(V)

'''
class Solution:
  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    heap = [] # min heap
    m = len(heights)
    n = len(heights[0])
    visit = [[False for _ in range(n)] for _ in range(m)]
    dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    heap.append([0, 0, 0]) # [effort, x, y]

    while heap:
      # expand
      curr = heapq.heappop(heap)
      effort, x, y = curr
      if visit[x][y]:
        continue
      else:
        visit[x][y] = True

      if x == m - 1 and y == n - 1:
        return effort

      # generate
      for d in dir:
        dx, dy = d
        x2 = x + dx
        y2 = y + dy
        if 0 <= x2 < m and 0 <= y2 < n:
          new_effort = max(effort, abs(heights[x2][y2] - heights[x][y]))
          heapq.heappush(heap, [new_effort, x2, y2])

    return -1

# test
sol = Solution()
h = [[1,2,2],[3,8,2],[5,3,5]]
res = sol.minimumEffortPath(h)
print(res)