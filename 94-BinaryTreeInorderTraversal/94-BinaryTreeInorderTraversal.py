# Last updated: 7/14/2026, 2:00:42 PM
class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)      # Visit left subtree
            result.append(node.val) # Visit root
            inorder(node.right)     # Visit right subtree

        inorder(root)
        return result