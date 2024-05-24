import heapq

class Cell:
  def __init__(self, row, col, val):
    self.row = row
    self.col = col
    self.val = val

  def __lt__(self, other):
    return self.val < other.val

class Solution(object):
  def kthSmallest(self, matrix, k):
    """
    input: int[][] matrix, int k
    return: int
    """
    # write your solution here
    # matrix size
    m = len(matrix)
    n = len(matrix[0])

    visit = [[ False for _ in range(n)] for _ in range(m)]
    for row in matrix:
      visit.append(row.copy())    

    # initial
    pq = [Cell(0, 0, matrix[0][0])]  # min heap, array of Cell
    visit[0][0] = True
    cnt = 0
    curr = None

    # terminate: iterate k rounds
    while  cnt < k:
      # expand 
      curr = heapq.heappop(pq)
      cnt += 1
      
      print(curr.val)

      # generate
      x = curr.row
      y = curr.col

      if x + 1 < m and not visit[x + 1][y]:
        heapq.heappush(pq, Cell(x + 1, y, matrix[x + 1][y]))
        visit[x + 1][y] = True

      if y + 1 < n and not visit[x][y + 1]:
        heapq.heappush(pq, Cell(x , y + 1, matrix[x][y + 1]))
        visit[x][y + 1] = True
      
    print(visit)
    return curr.val





# test
matrix = [[1,2],[1,3]]
sol = Solution()
res = sol.kthSmallest(matrix, 2)
print(res)