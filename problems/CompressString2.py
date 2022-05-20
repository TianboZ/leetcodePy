class Solution(object):
  def compress(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    i = 0
    arr = []
    while i < len(input):
      j = i
      while j < len(input) and input[j] == input[i]:
        j += 1

      arr.append(input[i])
      
      count = str( j - i)
      for digit in count:
        arr.append(digit)
      i = j

    return ''.join(arr)
      
sol = Solution()
res = sol.compress('aaaaaaaaaaaaaaaaab')
print(res)