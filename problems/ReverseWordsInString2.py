class Solution(object):
  def reverseWords(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    
    arr = list(input)

    self.reverseHelper(arr)
    return self.removeSpaces(arr)
  
  def reverseHelper(self, arr):
    fast = 0
    while fast < len(arr):
      if arr[fast] == ' ':
        fast += 1
      else:
        slow = fast
        while fast < len(arr) and arr[fast] != ' ':
          fast += 1 
        
        # fast - 1 is last letter of non ' '
        self.reverse(arr, slow, fast - 1)

    self.reverse(arr, 0, len(arr) - 1)

  def removeSpaces(self, arr):
    #  remove leading spaces
    left = 0
    while left < len(arr) and arr[left] == ' ':
      left += 1
   
    #  remove trailing spaces
    right = len(arr) - 1
    while right >= 0 and arr[right] == ' ':
      right -= 1

    # remove duplicate spaces
    fast = left + 1
    slow = left + 1
    while fast <= right:
      if arr[fast] == arr[slow - 1] and arr[fast] == ' ':
        fast += 1
      else:
        arr[slow] = arr[fast]
        slow += 1
        fast += 1

    print(arr)
    
    print(left - 1)
    print(slow)
    res = arr[left: slow]

    print(res)
    return ''.join(res)

  def reverse(self, arr, i, j):
    while i < j:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j -= 1


sol = Solution()
res = sol.reverseWords("    123    4")
print(res)