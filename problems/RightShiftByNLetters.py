class Solution(object):
  def rightShift(self, input, n):
    """
    input: string input, int n
    return: string
    """
    # write your solution here
    if not input: return ''
    move = n % len(input)
    if move == 0: return input

    arr = list(input)
    self.reverse(arr, 0, len(arr) - 1 - move)
    self.reverse(arr, len(arr) - move, len(arr) - 1)
    self.reverse(arr, 0, len(arr) - 1)

    return ''.join(arr)

  def reverse(self, arr, lo, hi):
    while lo < hi:
      arr[lo], arr[hi] = arr[hi], arr[lo]
      lo += 1
      hi -= 1