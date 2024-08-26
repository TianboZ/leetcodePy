# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        maxval = math.inf
        self.min1 = maxval
        self.min2 = maxval
        
        self.dfs(root)
        if self.min2 != maxval:
            return self.min2
        return -1
    
    def dfs(self, root):
        if not root:
            return
        
        if root.val < self.min1:
            self.min1 = root.val
        elif root.val < self.min2 and root.val > self.min1:
            self.min2 = root.val
            
        self.dfs(root.left)
        self.dfs(root.right)