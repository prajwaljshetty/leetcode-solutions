/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* evenOddBit(int n, int* returnSize) {
    *returnSize = 2;
    int* bits = calloc(*returnSize , sizeof(int));

    int index = 0;

    while((n >> index) > 0){
        if((n >> index) & 1){
            if((index % 2) == 0) bits[0]++;
            else bits[1]++;
        }
        index += 1;
    }

    return bits;
}