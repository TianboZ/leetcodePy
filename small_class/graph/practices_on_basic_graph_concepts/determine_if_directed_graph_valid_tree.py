'''
solution:
1. find root. root is node with in-degree = 0
  if multiple root found, not tree
2. DFS, mark visited for the node when first time visting
  if any node can be visited more than once, not tree
  if any node not reachable., not tree

'''