"""
soluton:
1. min heap, size K, store Cell class

Cell is class

Cell {
  i,  // index of array 1
  j,  // index of array 2
  m,  // index of array 3
  val,    // distance to (0 0 0)
}

2. iteralte 3 arrays
3. kth element popup from min heap is our solution


compexity: 
time O(log K * (a length + b length + c length))

"""


import heapq
  
class Solution(object):

  def closest(self, a, b, c, k):
    """
    input: int[] a, int[] b, int[] c, int k
    return: Integer[]
    """
    # write your solution here
    a_len = len(a)
    b_len = len(b)
    c_len = len(c)

    def getsum(i, j, k):
      return a[i] * a[i] + b[j] * b[j] + c[k] * c[k]

    # init
    heap = [[getsum(0, 0, 0), 0, 0, 0]]  # min heap, heap item: [value, x, y, z]
    cnt = 0
    print(heap)
    visit = set()
    
    # terminate
    while heap:
      # expand 
      curr = heapq.heappop(heap)
      print('curr=',curr)
      sum, x, y, z = curr

      hash = str([x, y, z])
      if hash in visit:
        continue

      visit.add(hash)
      print(visit)
      cnt += 1

      if cnt == k:
        return [a[x], b[y], c[z]]

      # generate
      if x + 1 < a_len and y < b_len and z < c_len:
        heapq.heappush(heap, [getsum(x + 1, y, z), x + 1, y, z])
      
      if x < a_len and y + 1 < b_len and z < c_len:
        heapq.heappush(heap, [getsum(x, y + 1, z), x, y + 1, z])
      
      if x < a_len and y < b_len and z + 1 < c_len:
        heapq.heappush(heap, [getsum(x, y, z + 1), x, y, z + 1])
      
    
    return [-1,-1,-1]
  
# test
a = [1, 3, 5]
b = [2, 4]
c = [3, 6]
sol = Solution()
res = sol.closest(a, b, c, 2)
print(res)


