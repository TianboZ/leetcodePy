# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
    map = {}  # <sum: freq>
    self.dfs(root, map)
    
    freq = max(map.values())
    res = []
    # build res
    for k, v in map.items():
      if v == freq:
        res.append(k)

    return res
  # return sum of root
  def dfs(self, root, map)->int:
    if not root:
      return 0

    left = self.dfs(root.left, map)
    right = self.dfs(root.right, map)
    sum = left + right + root.val

    map[sum] = map.get(sum, 0) + 1

    return sum
    