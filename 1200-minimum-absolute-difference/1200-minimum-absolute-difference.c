/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

 int comparator(const void* x ,const void* y){
    return ( (*((int *) x)) > (*((int *) y)) ) - ( ((*((int *) x)) < (*((int *) y))) );
 }

int** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int** returnColumnSizes) {
    qsort( arr , arrSize , sizeof(int) , comparator);

    int maxElement =   arrSize - 1 , minDiff = INT_MAX;
    int** minArray = malloc(maxElement * sizeof(int*));
    int* pairs = malloc(2 * maxElement * sizeof(int));
    *returnColumnSizes = malloc(maxElement * sizeof(int));

    for (int i = 0; i < maxElement; i++) {
        minArray[i] = pairs + 2 * i;
        (*returnColumnSizes)[i] = 2;
    }

    for( int i = 1 ; i < arrSize ; i++){
        int diff  = arr[i] - arr[i - 1];
        if((arr[i] > arr[i - 1] )&& (minDiff > diff )){
            minDiff = diff;
            *returnSize = 0;
        }

        if(diff == minDiff) {
            minArray[*returnSize][0] = arr[i - 1];
            minArray[*returnSize][1] = arr[i];
            (*returnSize)++;
        }
    }

    return minArray; 
}