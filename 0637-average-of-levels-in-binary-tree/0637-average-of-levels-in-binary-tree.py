# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root : 
            return

        levelSum = {}
        
        def traverse(node , level):
            if node is None : 
                return
            
            siblingSum , siblingCount = levelSum.get(level , (0 , 0))
            levelSum[level] =  (siblingSum + node.val , siblingCount + 1)

            traverse(node.left , level + 1)
            traverse(node.right , level + 1)

        traverse(root , 0)

        return [ levelSum[level][0] / levelSum[level][1] for level in levelSum]
    






        