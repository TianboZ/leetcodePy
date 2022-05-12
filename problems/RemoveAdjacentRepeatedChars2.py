class Solution(object):
  def deDup(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    if not input: return ''
    if len(input) == 2: return input

    arr = list(input)
    slow = 2
    fast = 2

    while fast < len(arr):
      if arr[slow - 2] == arr[fast]:
        fast += 1
      else:
        arr[slow] = arr[fast]
        slow += 1
        fast += 1
    

    return ''.join(arr[:slow])
