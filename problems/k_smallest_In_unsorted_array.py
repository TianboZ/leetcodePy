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
        # 无脑push, pop 
        heapq.heappush(pq, Cell(v))
        heapq.heappop(pq)
      

    while pq:
      res.append(heapq.heappop(pq).v)

    return res
  


# use min heap
class Solution2(object):
  def kSmallest(self, array, k):
    pq = []  # min heap
    
    for i in array:
      heapq.heappush(pq, i)      
      if len(pq) > k:
        heapq.heappop(pq)
    
    print(pq)



# test
sol = Solution()
res = sol.kSmallest([1, 2, 3, -1, 100, -2], 3)
print(res)


sol2 = Solution2()
sol2.kSmallest([1, 2, 3, -1, 100, -2], 3)