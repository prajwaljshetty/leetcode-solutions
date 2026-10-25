/**
 * Note: The returned array must be malloced, assume caller calls free().
 */



int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize) {
    int maxNums = 101;
    int frequency[101] = {0};

    *returnSize = numsSize;
    int* smallCountArray = calloc(*returnSize,sizeof(int));

    for(int i = 0 ; i < numsSize ; i++){
        frequency[nums[i]]++;
    }

    int count = 0;

    for (int i = 0; i < maxNums; i++) {
        int currentFrequency = frequency[i];
        frequency[i] = count;
        count += currentFrequency;
    }

    for(int i = 0 ; i < numsSize ; i++){
        smallCountArray[i] = frequency[nums[i]];
    }

    return smallCountArray;
}