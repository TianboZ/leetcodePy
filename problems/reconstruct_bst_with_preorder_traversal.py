from UtilityClasses import TreeNode


class Solution(object):
  def reconstruct(self, pre):
    """
    input: int[] pre
    return: TreeNode
    """
    # write your solution here
    if not pre: return None
    return self.dfs(0, len(pre) - 1, pre)

  def dfs(self, lo, hi, pre):
    # base case
    if lo > hi:
      return None

    # recursive rule 
    val = pre[lo]
    root = TreeNode(val)
    j = lo + 1
    while j < len(pre) and pre[j] < val :
      j += 1

    left = self.dfs(lo + 1, j - 1, pre)
    right = self.dfs(j, hi, pre)
    
    root.left = left
    root.right = right

    return root