class Solution(object): 
  def mergeSort(self, array):
    # base case
    if len(array) <= 1 or array is None: return array

    # recursive rule
    mid = len(array) // 2
    left = self.mergeSort(array[0:mid])
    right = self.mergeSort(array[mid:])

    print(array)

    return self.merge(array, left, right)


  def merge(self, arr, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i += 1
        k += 1
      else:
        arr[k] = right[j]
        j += 1
        k += 1

    while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1
    
    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1

    return arr

class Solution2:
  def mergeSort(self, arr):
    hi = len(arr) - 1
    self.sort(arr, 0, hi)
    return arr

  def sort(self, arr, lo, hi):
    # base case
    if lo >= hi: 
      return

    # recursive rule
    mid = (lo + hi) // 2
    self.sort(arr, lo, mid)
    self.sort(arr, mid + 1, hi)
    self.merge(arr, lo, hi)
  
  def merge(self, arr: list, lo: int, hi: int ):
    mid = (lo + hi) // 2
    i = lo
    j = mid + 1
    tmp = []
    while i <= mid and j <= hi:
      if arr[i] < arr[j]:
        tmp.append(arr[i])
        i += 1
      else:
        tmp.append(arr[j])
        j += 1
    
    while i <= mid:
      tmp.append(arr[i])
      i += 1
    while j <= hi:
      tmp.append(arr[j])
      j += 1
    
    # print('tmp', tmp, 'lo', lo, 'hi', hi)

    for i in range(len(tmp)):
      arr[i + lo] = tmp[i]

sol = Solution()
sol2 = Solution2()
# res = sol.mergeSort([-1,1, 10,-10])
arr = [1, -1, 2, 1, 100, -22]
sol2.mergeSort(arr)
print('sol:',arr)
