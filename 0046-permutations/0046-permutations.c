/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void swap(int *x , int *y){
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void genPermute(int *array , int start , int end ,int  **permutes , int *permuteIndex){
    if(start == end){
        memcpy(permutes[(*permuteIndex)++] , array , end * sizeof(int));
        return;
    }

    for( int i = start ; i < end ; i++ ){
        swap(&array[start],&array[i]);
        genPermute(array,start+1,end,permutes,permuteIndex);
        swap(&array[start],&array[i]);
    }
}

int factorial(int n){
    return n <= 1 ? 1 : n * factorial(n - 1);
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    *returnSize = factorial(numsSize);
    int **permutes = malloc( *returnSize * sizeof(int *));
    *returnColumnSizes = malloc( *returnSize * sizeof(int));

    for(int i = 0 ; i < *returnSize ; i++){
        permutes[i] = malloc(numsSize * sizeof(int));
        (*returnColumnSizes)[i] = numsSize;
    }
    int permuteIndex = 0;
    genPermute(nums,0,numsSize,permutes,&permuteIndex);

    return permutes;
}