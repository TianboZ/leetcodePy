from UtilityClasses import TreeNode

class Solution(object):
  def isBalanced(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    res = self.helper(root)
    return res >= 0
      
  # if balanced, return tree height; otherwise return -1
  def helper2(self, root):
    if not root: return 0

    left = self.helper2(root.left)
    right = self.helper2(root.right)

    if left == -1 or right == -1: return -1
    if abs(left - right) > 1: return -1
    return max(left, right) + 1
  
  # return tree height. if tree is not balanced, return -1
  def helper(self, root):
    if not root: return 0
    
    left = self.helper(root.left)
    right = self.helper(root.right)
    
    if left == -1 or right == -1: return -1
    
    if abs(left - right) >= 2: return -1
    
    return max(left, right) + 1
    

sol = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)

n1.left = n2
n2.left = n3
n1.right = n4

n3.left = TreeNode(5)

print(sol.isBalanced(n1))