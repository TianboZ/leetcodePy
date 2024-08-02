# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
solution:
- build graph
- run BFS find shortest path to any leaf node

complexity:
time O(n)
space O(n)

"""


class Solution:
  def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
    self.target = None
    adj = collections.defaultdict(list)
    self.dfs(root, None, adj, k)
    return self.bfs(self.target, adj)

  def dfs(self, root, prev, adj, k):
    if not root:
      return

    if root.val == k:
      self.target = root

    adj[root].append(prev)
    adj[prev].append(root)
    self.dfs(root.left, root, adj, k)
    self.dfs(root.right, root, adj, k)

  def bfs(self, root, adj) -> int:
    queue = deque([])
    visit = set()
    dis = 0

    # init
    queue.append(root)
    visit.add(root)

    # terminate
    while queue:
      # expand
      curr = queue.popleft()
      print('curr', curr.val)

      # detect leaf
      if not curr.left and not curr.right:
        return curr.val

      # generate
      for nei in adj.get(curr, []):
        if nei and nei not in visit:
          visit.add(nei)
          queue.append(nei)

    return -1
