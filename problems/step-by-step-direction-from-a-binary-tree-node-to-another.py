# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def getDirections2(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    # build graph
    graph = {} # <node, [[node, 'L'], [node, 'R']]>
    def getGraph(root, prev):
      if not root:
        return
      
      graph[root.val] = []
      if root.left:
        graph[root.val].append([root.left.val, 'L'])
      if root.right:
        graph[root.val].append([root.right.val, 'R'])
      if prev:
        graph[root.val].append([prev.val, 'U'])
        
      getGraph(root.left, root)
      getGraph(root.right, root)

    getGraph(root, None)
    # print(graph)
    
    # bfs
    visit = set()
    queue = deque([])
    prevMap = {}
    
    # initial
    queue.append([startValue, '']) # [node, dir]
    visit.add(startValue)

    # terminate
    while queue:
      # expand 
      node, dir = queue.popleft()
      if node == destValue:
        break
      
      # generate
      for nei in graph.get(node, []):
        node2, dir2 = nei
        if node2 not in visit:
          visit.add(node2)
          queue.append([node2, dir2])
          # print(node ,'->', node2, 'dir: ', dir2)
          prevMap[node2] = [node, dir2]

    # reconstruct path
    print(prevMap)
    node = destValue
    path = []
    while node != startValue:
      prev, dir = prevMap.get(node)
      path.append(dir)
      node = prev
    path.reverse()
    # print(path)

    return ''.join(path)


  def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    lca = self.getLca(root, startValue, destValue)
    print(lca.val)
    
    self.path = []
    self.findPath(lca, startValue, [])
    path1 = self.path.copy()
    
    self.path = []
    self.findPath(lca, destValue, [])
    path2 = self.path.copy()

    path1 = [ 'U' for _ in path1]
    res =  path1 + path2
    return ''.join(res)

  def findPath(self, root, end, path):
    # base case
    if not root:
      return
      
    if root.val == end:
      self.path = path.copy()
      return 

    # recursive rule
    path.append('L')
    self.findPath(root.left, end, path)
    path.pop()

    path.append('R')
    self.findPath(root.right, end, path)
    path.pop()



  # return None if not find r1 or r2 in the subtree
  def getLca(self, root, r1, r2) -> TreeNode:
    if not root:
      return None
    
    if root.val == r1 or root.val == r2:
      return root

    left = self.getLca(root.left, r1, r2)
    right = self.getLca(root.right, r1, r2)

    if left and right:
      return root
    
    if left:
      return left
    return right
    