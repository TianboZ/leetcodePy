class Solution(object):
  def deDup(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    fast = 0
    slow = 0
    arr = list(input)
    while fast < len(arr):
      fast2 = fast
      while fast2 + 1 < len(arr) and arr[fast2 + 1] == arr[fast]:
        fast2 += 1
      
      if fast2 == fast:
        arr[slow] = arr[fast]
        slow += 1
        fast += 1
      else:
        fast = fast2 + 1
    
    return ''.join(arr[:slow])


sol = Solution()
res = sol.deDup('aaaabb1')
print(res)