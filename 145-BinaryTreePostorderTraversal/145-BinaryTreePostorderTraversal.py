# Last updated: 7/14/2026, 2:00:27 PM
class Solution:
    def postorderTraversal(self, root):
        result = []

        def postorder(node):
            if not node:
                return

            postorder(node.left)    # Left subtree
            postorder(node.right)   # Right subtree
            result.append(node.val) # Root

        postorder(root)
        return result 