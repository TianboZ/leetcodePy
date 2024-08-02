class Solution:
  def maximumGain(self, s: str, x: int, y: int) -> int:
    arr = list(s)
    self.res = 0
    self.dfs(arr, x, y, 0)
    return self.res

  def dfs(self, arr, x, y, cnt):
    # base case
    hasAb = False
    for i in range(len(arr) - 1):
      if arr[i] == 'a' and arr[i + 1] == 'b' or  arr[i] == 'b' and arr[i + 1] == 'a':
        hasAb = True
        break
 
    if not hasAb:
      self.res = max(self.res, cnt)
      return 

    # recursive rule
    for i in range(len(arr) - 1):
      if arr[i] == 'a' and arr[i + 1] == 'b':
        # print('before', arr, 'cnt=', cnt)
        arr.pop(i)
        arr.pop(i)
        self.dfs(arr, x, y, cnt + x)
        arr.insert(i, 'b') 
        arr.insert(i, 'a') 
        # print('after', arr, 'cnt=', cnt)

      if arr[i] == 'b' and arr[i + 1] == 'a':
        arr.pop(i)
        arr.pop(i)
        self.dfs(arr, x, y, cnt + y)
        arr.insert(i, 'a') 
        arr.insert(i, 'b') 
        
      