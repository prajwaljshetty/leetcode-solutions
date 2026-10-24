/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructRectangle(int area, int* returnSize) {
    *returnSize = 2 ;
    int* combo = malloc(*returnSize * sizeof(int));
    
    combo[0] = INT_MAX;
    combo[1] = 0;

    for( int i = 1 ; i <= area ; i++ ){
        if((area % i) == 0 ){
            int tempL = i;
            int tempW = area / i;
            if( (tempL >= tempW) && (((tempL - tempW) < (combo[0] - combo[1]))) ){
                combo[0] = tempL;
                combo[1] = tempW;
            }
        }
    }

    return combo;

}