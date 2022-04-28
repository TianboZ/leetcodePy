import heapq

class Solution(object):
  def kSmallest(self, array, k):
    """
    input: int[] array, int k
    return: int[]
    """
    # write your solution here
    pq = [] # max heap
    for n in array:
      heapq.heappush(pq, -n)
      if len(pq) > k:
        heapq.heappop(pq)
    
    res = []
    while pq:
      res.append(-heapq.heappop(pq))
    res.reverse
    return res