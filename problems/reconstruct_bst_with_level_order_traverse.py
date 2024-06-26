from problems.UtilityClasses import TreeNode


class Solution(object):
  def reconstruct(self, level):
    """
    input: int[] level
    return: TreeNode
    """
    # write your solution here
    if not level:
      return None
    
    return self.dfs(level)

  def dfs(self, level):
    # base caes
    if not level:
      return None

    # recursive rule
    val = level[0]
    root = TreeNode(val)
    leftLevels = []
    rightLevels = []
    for i in range(1, len(level)):
      if level[i] < val:
        leftLevels.append(level[i])
      else:
        rightLevels.append(level[i])
    root.left = self.dfs(leftLevels)
    root.right = self.dfs(rightLevels)
    return root