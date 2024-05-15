"""
sol1: iterative
time: O(N)
space: O(N)

sol2: recursive
time O(N)
space O(1)
"""

class Solution(object):
  def reverse(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    arr = list(input)
    self.helper(arr, 0, len(input) - 1)
    return ''.join(arr)

  def helper(self, arr, lo, hi):
    # basecase
    if lo >= hi: return
    
    # recursive rule
    tmp =  arr[lo] 
    arr[lo] = arr[hi]
    arr[hi] = tmp

    self.helper(arr, lo + 1, hi - 1)

sol = Solution()
res = sol.reverse('1234')
print(res)