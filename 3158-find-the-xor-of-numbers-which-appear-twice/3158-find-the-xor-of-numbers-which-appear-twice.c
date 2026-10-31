int duplicateNumbersXOR(int* nums, int numsSize) {
    int xorMap[51] = {0};
    int dupXor = 0;

    for(int i = 0 ; i < numsSize ; i++){
        xorMap[nums[i]] ^= nums[i];
    }

    for(int i = 0 ; i < numsSize ; i++){
        if(xorMap[nums[i]] == 0) {
            dupXor ^= nums[i];
            xorMap[nums[i]] ^= nums[i];
        }
    }

    return dupXor;
}