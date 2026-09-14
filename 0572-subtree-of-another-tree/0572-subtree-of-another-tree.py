class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(node1, node2):
            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            return sameTree(node1.left, node2.left) and \
                   sameTree(node1.right, node2.right)

        def search(node):
            if node is None:
                return False

            if node.val == subRoot.val and sameTree(node, subRoot):
                return True

            return search(node.left) or search(node.right)

        return search(root)