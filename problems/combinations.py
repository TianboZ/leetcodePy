"""
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.

recurstion tree
        [1, 2 ,3 ,4]
        /   \   \   \
0:     [1]  [2] [3] [4]
       /   \
1:    [1,2] [1,3]

"""
from typing import List


class Solution:
  def combine(self, n: int, k: int) -> List[List[int]]:
    self.res = []
    arr = [i + 1 for i in range(n)]
    self.dfs(0, arr, [], k)
    return self.res

  def dfs(self, i, arr, path, k):
    # base case
    if len(path) == k:
      self.res.append(path.copy())
      return

    # recursive rule
    for j in range(i, len(arr)):
      path.append(arr[j])
      self.dfs(j + 1, arr, path, k)
      path.pop()

sol = Solution()
res = sol.combine(4, 2)
print(res)