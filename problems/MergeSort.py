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


sol = Solution()
res = sol.mergeSort([-1,1, 10,-10])
print('sol:',res)
