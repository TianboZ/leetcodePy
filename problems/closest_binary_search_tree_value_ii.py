# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
solution:
- inroder traverse the BST, record nodes, they are in increasing order
- do binary search in array, find k closest values

complexity:
time O(N)
space O(N)

"""
from bisect import bisect_left

class Solution:
  def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
    arr = []
    # get all nodes in increasing order
    self.dfs(root, arr)

    # run binary search, find largest smaller
    # lo = 0
    # hi = len(arr) - 1
    
    # while lo + 1 < hi:
    #   mid = lo + (hi - lo) // 2
    #   if arr[mid] == target:
    #     hi = mid
    #   elif arr[mid] < target:
    #     lo = mid
    #   else:
    #     hi = mid

    lo = 0
    hi = 1
    i = bisect_left(arr, target) - 1
    if i >= 0:
      lo = i
      hi = lo + 1

    print(arr, lo, hi)
    cnt = 0
    res = []
    
    while cnt < k:
      if hi == len(arr) or  (abs(arr[lo] - target) <= abs(arr[hi] - target)) :
        res.append(arr[lo])
        lo -= 1
      else:
        res.append(arr[hi])
        hi += 1
      cnt += 1
    
    print('res:', res)
    return res

  def dfs(self, root, arr):
    if not root:
      return

    self.dfs(root.left, arr)
    arr.append(root.val)
    self.dfs(root.right, arr)