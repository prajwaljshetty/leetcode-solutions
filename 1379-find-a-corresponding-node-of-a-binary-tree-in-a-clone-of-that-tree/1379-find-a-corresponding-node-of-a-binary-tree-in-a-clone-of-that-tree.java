/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    TreeNode dfs( TreeNode currentNode , TreeNode target ){
        if (currentNode == null) 
            return null;
        if( currentNode.val == target.val) 
            return currentNode;
        TreeNode leftNode = dfs(currentNode.left, target);
        if( leftNode == null ) 
            return dfs(currentNode.right, target);
        return leftNode;
    }

    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        return dfs(cloned,target);
    }
}