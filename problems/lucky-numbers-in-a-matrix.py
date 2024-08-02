"""
solution:
- find min per row   [[val, col index], [], [], ...]
- find max per col   [val, val2, ...]
- iterate each element in row

complexity:
time O(m*n)
space O(m*n)

"""
class Solution:
  def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
    row = []
    col = []
    
    m = len(matrix)
    n = len(matrix[0])
    
    for r in matrix:
      minval = [1000000, -1]
      for i in range(n):
        if r[i] < minval[0]:
          minval = [r[i], i]
      row.append(minval)

    for j in range(n):
      maxval = -100000
      for i in range(m):
        maxval = max(matrix[i][j], maxval)
      col.append(maxval)
      # print(cols)

    # print(rows, cols)
    # find solution
    res = []
    for minval, colIndex in row:
      if minval == col[colIndex]:
        res.append(minval)
    
    return res