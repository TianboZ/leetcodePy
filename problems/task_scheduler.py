from collections import Counter, deque
import heapq
from typing import List


class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    map = Counter(tasks)
    print('map', map, 'values', map.values(), 'values', map.keys(), 'items', map.items())
    values = map.values()
    maxheap = [-v for v in values]
    heapq.heapify(maxheap)
    queue = deque([])
    time = 0

    while maxheap or queue:
      time += 1
      if maxheap:
        curr = heapq.heappop(maxheap)  # e.g. -3
        curr += 1   # e.g.    -3 -> -2, freq decrease

        if curr: 
          queue.append([curr, time + n])

      if queue and queue[0][1] == time:
        task = queue.popleft()
        heapq.heappush(maxheap, task[0])
      
    return time

class Solution2:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    map = Counter(tasks)
    maxheap = []
    for k, v in map.items():
      maxheap.append([-v, k])  # [freq, task name]
    heapq.heapify(maxheap)
    queue = deque([])

    path = []
    time = 0
    while maxheap or queue:
      print(maxheap)
      time += 1
      if maxheap:
        curr = heapq.heappop(maxheap)
        task = curr[1]
        path.append(task)
        cnt = curr[0]
        cnt += 1
      
        if cnt:
          queue.append([cnt, time + n, task]) # [cnt, next time can do it, task name]
      else:
        path.append("")

      if queue and queue[0][1] == time:
        curr = queue.popleft()
        heapq.heappush(maxheap, [curr[0], curr[2]])

    print(path)
    return time



sol = Solution2()
tasks = ['a', 'c', 'a', 'b', 'd', 'b' ]
res = sol.leastInterval(tasks, 2)
print(res)


