"""
2 pointers:

[0, slow): keey
[slow, fast]: removed
[fast, end]: explore

"""
class Solution(object):
  def remove(self, input, t):
    """
    input: string input, string t
    return: string
    """
    # write your solution here
    chars = set(t)
    arr = list(input)

    slow = 0
    fast = 0

    while fast  < len(arr):
      c = arr[fast]
      if c in chars:
        fast += 1
      else:
        arr[slow] = arr[fast]
        slow += 1
        fast += 1
    
    arr = arr[0:slow]
    return ''.join(arr)