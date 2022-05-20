class Solution(object):
  def reverseWords(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    arr = list(input)

    fast = 0
    while fast < len(arr):
      if arr[fast] != ' ':
        slow = fast
        while  fast < len(arr) and arr[fast] != ' ':
          fast += 1
        
        # now fast - 1 is last index of non ' ' letter
        self.reverse(arr, slow, fast - 1)
      else:
        fast += 1

    
    self.reverse(arr, 0, len(arr) - 1)
    return ''.join(arr)


  def reverse(self, arr, i, j):
    while i < j:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j -= 1


sol = Solution()
res = sol.reverseWords('1 234')
print(res)