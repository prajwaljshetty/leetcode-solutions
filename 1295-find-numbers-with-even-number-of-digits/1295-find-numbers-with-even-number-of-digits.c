int findNumbers(int* nums, int numsSize) {
    int count = 0;
    for(int i = 0 ; i < numsSize ; i++){
        int digitcount = 0;
        while( nums[i] > 0 ){
            digitcount++;
            nums[i] /= 10;
        }
        if( (digitcount % 2) == 0) count++;
    }
    return count;
}