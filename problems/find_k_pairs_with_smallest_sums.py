'''
solution:
1 7 11
2 4 6
[1,2] is 1st pair, but we dont know [1+4] or [2+7] is smaller
use min heap, size = K. heap store [(nums[i] + nums[j]), i, j]

complexity:
in worst case, k == m * n
time: O(klogk)
space: O(k)
'''
import heapq

class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    minheap = []
    res = []
    visit = set()
    # init
    minheap.append([nums1[0] + nums2[0], 0, 0])
    visit.add((0, 0))

    while minheap:
      curr= heapq.heappop(minheap)
      sum, i, j = curr
      pair = [nums1[i], nums2[j]]
      res.append(pair)

      if len(res) == k:
        return res

      if i + 1 < len(nums1) and (i + 1, j) not in visit:
        heapq.heappush(minheap, [nums1[i + 1] + nums2[j], i + 1, j]) 
        visit.add((i + 1, j))

      if j + 1 < len(nums2) and (i, j + 1) not in visit:
        heapq.heappush(minheap, [nums1[i] + nums2[j + 1], i, j + 1])
        visit.add((i, j + 1))
        
    return res