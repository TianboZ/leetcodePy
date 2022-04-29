import heapq

class Cell():
  def __init__(self, x, y, val):
    self.x = x
    self.y = y
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
        
    m = len(matrix)
    n = len(matrix[0])
    
    pq = [] # min heap
    visit = [[False for i in range(n)] for i in range(m)] 
    cnt = 0
    # initial
    heapq.heappush(pq, Cell(0, 0, matrix[0][0]))
    visit[0][0] = True

    # terminate
    while pq:
      curr = heapq.heappop(pq)
      cnt += 1

      if cnt == k: return curr.val
      newx = curr.x + 1
      newy = curr.y

      if (newx >= 0 and newx < m) and not visit[newx][newy]:
        heapq.heappush(pq, Cell(newx, newy, matrix[newx][newy]))
        visit[newx][newy] = True

      newx = curr.x
      newy = curr.y + 1

      if (newy >= 0 and newy < n) and not visit[newx][newy]:
        heapq.heappush(pq, Cell(newx, newy, matrix[newx][newy]))
        visit[newx][newy] = True

    return 0


