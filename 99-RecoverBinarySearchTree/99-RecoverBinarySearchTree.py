# Last updated: 7/14/2026, 2:00:35 PM
class Solution:
    def recoverTree(self, root):
        nodes = []

        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)

        inorder(root)

        first = second = None
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                if first is None:
                    first = nodes[i]
                second = nodes[i + 1]

        first.val, second.val  = second.val, first.val
        