class Solution:
  def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':


  def dfs(self, root, prev):
    if not root:
      return
    
    self.dfs(root.left, root)
    prev.right = root
    root.left = prev
    prev = root
    
    self.dfs(root.right, root)

