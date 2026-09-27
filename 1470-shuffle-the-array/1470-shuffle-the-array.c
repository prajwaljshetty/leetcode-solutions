/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int *shuffledArray = malloc( numsSize * sizeof( int ));
    int indexX = 0 , indexY = 0 ;

    while( indexY < n ){
        shuffledArray[indexX++] = nums[indexY];
        shuffledArray[indexX++] = nums[ n + indexY++];
    }

    *returnSize = numsSize;
    return shuffledArray;
}

