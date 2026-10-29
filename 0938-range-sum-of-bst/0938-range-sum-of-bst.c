void sum(struct TreeNode* node , int* rangeSum , int low , int high){
    if(node == NULL) return;

    if(node->val >= low && node->val <= high) 
        *rangeSum += node->val;

    sum(node->left , rangeSum , low , high);
    sum(node->right , rangeSum , low , high);
 }
int rangeSumBST(struct TreeNode* root, int low, int high) {
    int rangeSum = 0;
    sum(root , &rangeSum , low , high);
    return rangeSum;
}