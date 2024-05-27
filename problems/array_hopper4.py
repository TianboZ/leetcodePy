
'''
solution:
Dijk

complexity:
m = array size
time: O(m * log m)
space: O(m)

'''
import heapq


class Solution(object):
  def minJump(self, array, index):
    """
    input: int[] array, int index
    return: int
    """
    # write your solution here
    # initial
    heap = [[0, index]] # min heap, [total jumps from start index, index]
    visit = {}

    # terminate
    while heap:
      # expand 
      curr = heapq.heappop(heap)
      curr_steps, curr_i = curr

      if curr_i in visit:
        continue

      print(curr)
      visit[curr_i] = curr_steps
      if curr_i == len(array) - 1:
        return visit[curr_i]

      # genearte
      maxsteps = array[curr_i]
      for j in range(curr_i - maxsteps, curr_i + maxsteps + 1):
        if j >= 0 and j < len(array):
          heapq.heappush(heap, [curr_steps + 1, j])

    return -1

# test
sol = Solution()
arr = [1, 3,1,2,2]
res = sol.minJump(arr, 2)
print(res)