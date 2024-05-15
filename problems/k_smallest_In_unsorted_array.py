import heapq

'''
solution:
maintain size = k max heap

time:
O(n * logK)

space:
O(K)

'''
# max heap item
class Cell(object):
  def __init__(self, v):
    self.v = v
  def __lt__(self, other):
    return self.v > other.v

class Solution(object):
  def kSmallest(self, array, k):
    """
    input: int[] array, int k
    return: int[]
    """
    # write your solution here
    res = []
    pq = [] # array of Cell

    for i, v in enumerate(array):
      if i < k:
        # first K element
        pq.append(Cell(v))
        heapq.heapify(pq)
      else:
        if len(pq) > 0 and  v < pq[0].v:
          heapq.heappop(pq)
          heapq.heappush(pq, Cell(v))
      

    while pq:
      res.append(heapq.heappop(pq))

    return res