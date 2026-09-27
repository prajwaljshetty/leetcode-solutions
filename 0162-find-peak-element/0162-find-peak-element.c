int findPeakElement(int* nums, int numsSize) {
    int maxIndex = 0;
    for( int i = 1 ; i < numsSize ; i++ ){
        if(nums[maxIndex] < nums[i]) maxIndex = i;
    }
    return maxIndex;
}