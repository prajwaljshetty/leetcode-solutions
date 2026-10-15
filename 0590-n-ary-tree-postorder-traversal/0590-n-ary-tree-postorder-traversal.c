/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int traverse(struct Node *node , int *array , int curr){
    if (node == NULL) return 0;
    int length = 0;
    for( int i = 0 ; i < (node->numChildren) ; i++ ){
        length += traverse((node->children)[i] , array , curr + length );
    }
    array[ curr + length ] = node->val;
    return  length + 1 ;
}

int* postorder(struct Node* root, int* returnSize) {
    int *array = malloc( 10000 * sizeof(int) );
    *returnSize = traverse(root,array,0);
    return array;
}


