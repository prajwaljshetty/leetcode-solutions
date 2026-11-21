# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        leftLeafs , rightLeafs = [] , []

        def traverse(node , leafs) :
            if node is None : 
                return
            if node.left is None and node.right is None :
                leafs.append(node.val)
            
            traverse(node.left , leafs)
            traverse(node.right , leafs)
        
        traverse(root1 , leftLeafs)
        traverse(root2 , rightLeafs)
        
        return leftLeafs == rightLeafs