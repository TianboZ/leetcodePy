"""
sol1: iterative

sol2: recursive
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
    arr[lo], arr[hi] = arr[hi], arr[lo]

    self.helper(arr, lo + 1, hi - 1)

sol = Solution()
res = sol.reverse('1234')
print(res)