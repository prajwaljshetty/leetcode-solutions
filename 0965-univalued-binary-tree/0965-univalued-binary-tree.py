# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:

        def traverse(node , value) :
            if node is None :
                return True
            
            return node.val == value and traverse(node.left , value) and traverse(node.right , value)
        
        return True if root is None else traverse(root , root.val)
            
        