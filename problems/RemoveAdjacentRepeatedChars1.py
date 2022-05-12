"""
[0, slow): keep
[slow, fast]: removed
[fast, end]: unknown

"""
class Solution(object):
  def deDup(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    slow = 1
    fast = 1

    arr = list(input)

    while fast < len(arr):
      if arr[slow - 1] == arr[fast]:
        fast += 1
      else:
        
        arr[slow] = arr[fast]
        slow += 1
        fast += 1

    return ''.join(arr[:slow])