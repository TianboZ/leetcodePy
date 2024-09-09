import heapq
from typing import List

class Solution:
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    minheap = []  # e.g. [[val, i, j], [val2, i2, j2], ...]    val = nums[i][j]
    maxVal = -100000  # Equivalent to Integer.MIN_VALUE
    res = [0, 0]
    rangeVal = 1000000  # A very large number for the initial range
    
    # Initialize the priority queue with the first element from each list
    for i in range(len(nums)):
      val = nums[i][0]
      maxVal = max(maxVal, val)
      heapq.heappush(minheap, [val, i, 0])
    
    # Continue until the priority queue has elements from all lists
    while len(minheap) == len(nums):
      curr = heapq.heappop(minheap)
      currMinVal, i, j = curr
      
      # Update the range if a smaller range is found
      if maxVal - currMinVal < rangeVal:
        res = [currMinVal, maxVal]
        rangeVal = maxVal - currMinVal
      
      # If the current list has more elements, add the next element to the priority queue
      if j + 1 < len(nums[i]):
        nextVal = nums[i][j + 1]
        heapq.heappush(minheap, [nextVal, i, j + 1])
        maxVal = max(maxVal, nextVal)
  
    return res
  
nums = [
  [4, 10, 15, 24, 26],
  [0, 9, 12, 20],
  [5, 18, 22, 30]
]

sol = Solution()
result = sol.smallestRange(nums)
print(result)  # Expected output: [20, 24]