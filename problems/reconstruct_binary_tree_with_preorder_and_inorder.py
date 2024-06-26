from UtilityClasses import TreeNode


class Solution(object):
  def reconstruct(self, inOrder, preOrder):
    """
    input: int[] inOrder, int[] preOrder
    return: TreeNode
    """
    # write your solution here

    size = len(inOrder)
    map = {} # key: inorder value       value: index
    for i in range(size):
      map[inOrder[i]] = i
    
    return self.dfs(preOrder, 0, size - 1, inOrder, 0, size - 1, map)

  def dfs(self, preorder, preL, preR, inorder, inL, inR, map):
    # base case
    if preL > preR:
      return None
    
    print(map)

    # recursive rule
    root = TreeNode(preorder[preL])
    index = map[preorder[preL]]
    leftSubTreeSize = index - inL
    root.left = self.dfs(preorder, preL + 1, preL + leftSubTreeSize, inorder, inL, index - 1, map)
    root.right = self.dfs(preorder, preL + leftSubTreeSize + 1, preR, inorder,  index + 1, inR, map)

    return root
  

sol = Solution()
preorder = [1,2, 4,5,3]
inorder = [4,2,5,1,3]
sol.reconstruct(inorder, preorder)
