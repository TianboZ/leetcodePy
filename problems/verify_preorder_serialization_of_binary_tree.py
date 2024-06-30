class Solution(object):
  def isValidSerialization(self, preorder):
    """
    input: string preorder
    return: boolean
    """
    # write your solution here
    self.i = 0 # preorder index
    preorder = preorder.split(",")
    print(preorder)
    res = self.dfs(preorder)

    # check if used up all slot
    return res and self.i == len(preorder)
  
  def dfs(self, preorder)->bool:
    # baes case
    if self.i >= len(preorder):
      return False

    # recursive rule
    v = preorder[self.i]
    self.i += 1

    if v == '#':
      return True
    else:
      # check next and next next slot
      return self.dfs(preorder) and self.dfs(preorder)


