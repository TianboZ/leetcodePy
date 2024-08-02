'''
[[4, 7],  [10, 11],     [13, 15]]
covers
[4,5,6,7,   10, 11,     13,14,15]


given cover list index 2 (6), remove 6, get:
[[4, 5], [7, 7], same ]


'''

class Solution:
  def remove(self, interval: list[list[int]], removeIdx):
    start = 0
    end = -1
    for i, arr in enumerate(interval):
      start = end + 1
      size = arr[1] - arr[0] + 1
      end = start + size - 1

      # case 0
      if arr[0] == arr[1] and removeIdx == start:
        interval.pop(i)
        break

      # case 1 
      if removeIdx == start:
        arr[0] = arr[0] + 1
        if len(arr) == 0:
          interval.pop(i)
        break

      # case 2 
      if removeIdx == end:
        print('end', end, 'arr', arr)

        arr[1] = arr[1] - 1
        if len(arr) == 0:
          interval.pop(i)
        break

      # case 3
      if start < removeIdx < end:
        # index:   4  5  6  7
        #         [1, 2, 3, 4]
        #                i
        
        diff = removeIdx - start
        x = arr[0] + diff - 1
        leftRange = [arr[0], x]
        rightRange = [x + 2, arr[1]]
        interval.pop(i)
        interval.insert(i, rightRange)
        interval.insert(i, leftRange)

        break

    print(interval)

sol = Solution()

'''
        1 , 2, 4, 5

index   0   1  2  3
''' 
sol.remove([[1,2], [5,5]], 2 )
sol.remove([[1,2], [4,7], [10, 10]], 3 )
sol.remove([[4, 7],[10, 11], [13, 15]], 0)