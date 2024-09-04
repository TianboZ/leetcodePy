
from typing import List

'''
soluiton;
dynamic programming

transformation function:
opt[i] = max(opt[i - 1] + nums[i], nums[i])
opt[i] means the sum of subarray that including nums[i]

complexity:
n is lenght of array 
O(n)

'''

def maxSubArray(self, nums: List[int]) -> int:
  opt = []
  opt.append(nums[0])
  maxx = nums[0]
  
  for i in range(1, len(nums)):
    n = nums[i]
    opt.append(max(opt[i - 1] + n, n))
    
    # updage global max
    maxx = max(maxx, max(opt[i - 1] + n, n))
  
  return maxx

arr = []
    
  

    