# Last updated: 7/14/2026, 2:00:36 PM
class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))





