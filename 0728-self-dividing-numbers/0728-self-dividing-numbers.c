/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* selfDividingNumbers(int left, int right, int* returnSize) {
    int *array = malloc( right * sizeof(int) );
    int index = 0 , num , digit;
    for( int i = left ; i <= right ; i++){
        num = i;
        while( num > 0 ){
            digit = num % 10;
            if( !digit || (i % digit) != 0) break;
            num /= 10;
        }
        if( num == 0 ) array[index++] = i;
    }
    
    *returnSize = index;
    return array;
}