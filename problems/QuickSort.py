import random

class Solution(object):
  def quickSort(self, array):
    return self.sort(array, 0, len(array) - 1)
  
  def sort(self, arr, lo, hi):
    # base case 
    if lo >= hi: return arr

    #  recursive rule
    piIdx = self.partition(arr, lo, hi)
    self.sort(arr, lo, piIdx - 1)
    self.sort(arr, piIdx + 1, hi)
    return arr

  def swap(self, arr, i, j):
     (arr[i], arr[j]) = (arr[j], arr[i])

  def partition(self, arr, lo, hi):
    pi = random.randrange(lo, hi)
    i = lo
    j = hi - 1
    pivot = arr[pi]
    
    # swap 
    self.swap(arr, hi, pi)

    # 挡板问题，同相而行
    # [0, i): <= pivot      [i, j]: unknown     (j, hi]:   > pivot
    while i <= j:
      if arr[i] <= pivot:
        i += 1
      elif arr[j] > pivot:
        j -= 1
      else:
        self.swap(arr, i, j)
        i += 1
        j -= 1

    self.swap(arr, i, hi)

    return i

sol = Solution()
res = sol.quickSort([1,2,-10,100])
print(res)

