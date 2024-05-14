'''
time: 
10:17 
10: 38

solution:

      121
      /  \
     A21   X1
    /  \     \
   AB1  AY    XA
  /   
  ABA  

time:
n is length of input array

O(branch ^ level)
O(2 ^ n)

space:
O(n)

'''

class Solution:
  def decode(self, arr):
    # sanity check, skip

    #  key: 1-26  value: a-z
    map = {i: chr(96 + i) for i in range(1, 27)}
    print(map)
    
    path = []
    self.dfs(arr, 0, path, map)

  def dfs(self, arr, i, path, map):
    # base case
    if i == len(arr):
      print(''.join(path))
      return

    # recursive rule
    # decode 1 digit
    digit = arr[i]
    path.append(map.get(digit))
    self.dfs(arr, i + 1, path, map)
    path.pop()

    # decode 2 digits
    if i + 1 < len(arr):
      #  e.g. arr is [3, 1]. firstly, we need to get number 31, then decode 31
      digit = arr[i] * 10 + arr[i + 1]  # 31
      if digit in map:
        path.append(map.get(digit))
        self.dfs(arr, i + 2, path, map)
        path.pop()

# test 
sol = Solution()
sol.decode([9, 1, 1])