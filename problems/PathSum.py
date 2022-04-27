class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum, 0)

    def helper(self, root, target, currSum):
        if not root:
            return False

        if not root.left and not root.right:
            if target == currSum + root.val:
                return True

        ans = self.helper(root.left, target, currSum + root.val) \
          or self.helper(root.right, target, currSum + root.val)
        return ans
