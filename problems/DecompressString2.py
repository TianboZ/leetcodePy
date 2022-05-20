class Solution(object):
  def decompress(self, input: str):
    """
    input: string input
    return: string
    """
    # write your solution here
    arr = list(input)
    i = 0
    char = ''
    res = []
    while i < len(arr):
      
      if arr[i].isnumeric():
        j = i
        while j < len(arr) and arr[j].isnumeric():
          j += 1
        num = ''.join(arr[i: j])
        num = int(num)
        count = 0
        while count < num:
          res.append(char)
          count += 1
        i = j
      else:
        char = arr[i]
        i += 1

    return ''.join(res)

sol = Solution()
res = sol.decompress('a0b10c2')
print(res)