/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getFinalState(int* nums, int numsSize, int k, int multiplier, int* returnSize) {

    for(int i = 0 ; i < k ; i++){
        int min = 0;
        for(int j = 0 ; j < numsSize ; j++){
            if(nums[min] > nums[j]) min = j;
        }
        nums[min] *= multiplier;
    }

    *returnSize = numsSize;
    return nums;
}