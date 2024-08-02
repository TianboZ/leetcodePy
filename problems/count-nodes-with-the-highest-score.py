class Solution:
  def countHighestScoreNodes(self, parents: List[int]) -> int:
    tree = { i: [] for i in range(len(parents))}
    
    # build tree
    for i in range(len(parents)):
      p = parents[i]
      if p in tree:
        tree[p].append(i)

    # print('tree', tree)  
    maxscore = -1
    scoremap = {}
    
    for i in range(len(parents)):
      # print('node, ', i)
      self.val = 1
      size = self.dfs(tree, 0, i)
      if size > 0:
        self.val *= size

      if self.val in scoremap:
        scoremap[self.val].append(i)
      else:
        scoremap[self.val] = [i]
      
      # print('score, ', self.val)
      maxscore = max(maxscore, self.val)
    
    return len(scoremap[maxscore])

  # target is node to delete, return tree size after delete target node
  def dfs(self, tree, root, target) -> int:
    # basecase
    if root not in tree:
      return 0

    # recursive rule
    sizes = []
    for child in tree.get(root, []):
      size = self.dfs(tree, child, target)
      if size > 0:
        sizes.append(size)

    if root == target:
      # print(sizes)
      for s in sizes:
        self.val *= s
      return 0
    
    return sum(sizes) + 1