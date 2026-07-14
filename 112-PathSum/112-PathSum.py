# Last updated: 7/14/2026, 2:00:32 PM
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        
        if not root.left and not root.right:
            return targetSum == root.val

        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
                