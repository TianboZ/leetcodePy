import heapq
import math

class Solution(object):
  def kth(self, k):
    """
    input: int k
    return: long
    """
    # write your solution here
    heap = []  # min heap, item: [val, x, y, z]
    heap.append([self.get_val(1, 1, 1), 1, 1, 1])
    visit= set()

    cnt = 0
    while heap:
      # expand
      curr = heapq.heappop(heap)
      cnt += 1
      val1, x1, y1, z1 = curr

      if cnt == k - 1:
        return val1
        
      # generate
      x2 = x1 + 1
      y2 = y1
      z2 = z1
      next = [x2, y2, z2]
      if str(next) not in visit:
        heapq.heappush(heap, [self.get_val(x2, y2, z2), x2, y2, z2])
        visit.add(str(next))

      x2 = x1
      y2 = y1 + 1
      z2 = z1
      next = [x2, y2, z2]
      if str(next) not in visit:
        heapq.heappush(heap, [self.get_val(x2, y2, z2), x2, y2, z2])
        visit.add(str(next))

      x2 = x1
      y2 = y1
      z2 = z1 + 1
      next = [x2, y2, z2]
      if str(next) not in visit:
        heapq.heappush(heap, [self.get_val(x2, y2, z2), x2, y2, z2])
        visit.add(str(next))

  def get_val(self, x, y, z):
    return math.pow(3, x) * math.pow(5, y) * math.pow(7, z)
  

  # test
sol = Solution()
res = sol.kth(10)
print(res)
  