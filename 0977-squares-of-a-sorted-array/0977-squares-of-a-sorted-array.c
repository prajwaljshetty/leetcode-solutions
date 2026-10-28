/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int i = 0 , j = numsSize -1;
    int square1 , square2;
    
    int* result = malloc( numsSize * sizeof(int));
    int k = j;

    while(i <= j){
        square1 = nums[i] * nums[i];
        square2 = nums[j] * nums[j];
        if( square1 > square2){
            result[k--] = square1;
            i++;
        }else{
            result[k--] = square2;
            j--;
        }
    }

    *returnSize = numsSize;
    return result;
}