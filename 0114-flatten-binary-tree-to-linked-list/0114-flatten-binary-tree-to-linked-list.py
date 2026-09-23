# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:

        def last_right_child( node ) :
            if node.right is None :
                return node
            else :
                return last_right_child( node.right )

        def dfs( node ) :
            if node is None : return None

            if node.right is None :
                node.right = node.left
                node.left = None
                dfs( node.right )
            elif node.left is not None :
                last_child =  last_right_child( node.left )
                last_child.right = node.right
                node.left , node.right = None , node.left
                dfs( node.right )
            else :
                dfs( node.right )
                
               
        dfs( root )