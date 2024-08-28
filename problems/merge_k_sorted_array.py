"""
solution:
- use size = k minheap to store smallest value of each array. e.g. [[val, row, col], [val2, row2, col2]...   ]
- pop smallest from minheap
- find next element
- insert to minheap 

complexity:

k = arrays count
n = total elements 

time: O(n * logk)
space: O(K)

"""
import heapq

class Solution(object):
  def merge(self, arrayOfArrays):
    """
    input: int[][] arrayOfArrays
    return: int[]
    """
    # write your solution here
    
    # init min heap
    minheap = []
    for row in range(len(arrayOfArrays)):
      arr = arrayOfArrays[row]
      if arr:
        minheap.append([arr[0], row, 0])
    
    heapq.heapify(minheap)
    
    # iterate all elements
    res = []
    while minheap:
      curr = heapq.heappop(minheap)
      val, row, col = curr
      res.append(val)
      
      if col + 1 < len(arrayOfArrays[row]):
        heapq.heappush(minheap, [arrayOfArrays[row][ col + 1], row, col + 1])
      
    print(res)
    return res
    
sol = Solution()
arr = [
  [1, 2, 3],
  [-1, 4],
  [10, 11, 12]
]
sol.merge(arr)

      