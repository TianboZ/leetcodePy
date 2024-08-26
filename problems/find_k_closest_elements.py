from typing import List

from bisect import bisect_left

"""
solution:
- binary search find largest elemnt < x, find lo, hi 
- 2 pointers, lo, hi. find K elements

complexity:
time O(logn + k)
space O(1)

"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sanity check
        if not arr or len(arr) == 0:
            return 

        # (lo, hi) exluding
        # lo = self.helper2(arr, x) 
        # hi = lo + 1
        
        # find largest smaller element than x
        lo = bisect_left(arr, x) - 1
        hi = lo + 1

        print(lo, hi)
        cnt = 0

        while cnt < k:
            if lo >= 0 and hi < len(arr):
                if abs( arr[lo] - x) <= abs( arr[hi] - x):
                    lo -= 1
                else:
                    hi += 1
            elif lo < 0:
                hi += 1
            else:
                lo -= 1

            cnt +=1

        return arr[lo + 1: hi]
      
    #  find largest element < x
    def helper2(self, arr, x):
        lo = 0
        hi = len(arr) - 1

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == x:
                hi = mid
            elif arr[mid] > x:
                hi = mid
            else:
                lo = mid

        if arr[hi] < x: return hi
        if arr[lo] < x: return lo
        return -1
        


'''
solution:
sort with custom comparator

complexity:
n is array length 
time  O(nlogn + klogk)
space (1)

'''
class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sanity check
        if not arr or len(arr) == 0:
            return []
        
        arr.sort(key=lambda num: abs(num - x) )

        # build ans
        res = []
        for i in range(k):
            res.append(arr[i])
        
        res.sort()
        return res

sol =  Solution()
res = sol.findClosestElements([1,2.1, 3.1, 4,5], 2, 3.1)
print(res)

sol2 = Solution2()
sol2.findClosestElements([1, 2.1, 3.1, 4, 5], 2, 3.1)