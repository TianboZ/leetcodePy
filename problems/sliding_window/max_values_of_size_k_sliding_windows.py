from collections import deque
import heapq

"""
solution:
monotonic deque
        [1, 2, 1, 0, 3]
 
queue   [1]       lo: 0, hi:0
        [2]       lo: 0, hi:1
        [2, 1]    lo: 1, hi:2
        [1]       lo: 2, hi:3
        [1, 0]  
        []
        [3]   

solution2:
sliding window use maxheap to represent

complexity
n is array length
time: O(n * logk)  有问题，maxheap size可能超过K

"""
class Solution:
  # optimal solution
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    lo = 0
    hi = 0
    queue = deque([])
    res = []

    while hi < len(nums):
      # handle right
      while queue and nums[queue[-1]] <  nums[hi]:
        queue.pop()
      queue.append(hi)

      # handle left
      if queue[0] <= hi - k:
        queue.popleft() 

      # current window
      if hi - lo + 1 == k:
        res.append(nums[queue[0]])
        lo += 1

      hi += 1
    return res

  def maxWindows2(self, array, k):
    """
    input: int[] array, int k
    return: Integer[]
    """
    # write your solution here

    hi = 0
    lo = 0
    res = []
    maxheap = []  # heap item: [array[i], i]

    while hi < len(array):
      # handle right bound
      heapq.heappush(maxheap, [-array[hi], hi])

      # handle left bound
      while maxheap and maxheap[0][1] <= hi - k:
        heapq.heappop(maxheap)
      
      # check current window
      if hi >= k - 1:
        res.append(-maxheap[0][0])

      hi += 1

    print(res)
    return res

sol = Solution()
sol.maxWindows2([1, 2, -3 ,4, 100, 0], 2)