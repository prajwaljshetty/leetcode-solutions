int findLucky(int* arr, int arrSize) {
    int frequency[501] = {0};

    for( int i = 0 ; i < arrSize ; i++) frequency[arr[i]]++;

    for(int i = 500 ; i > 0 ; i--){
        if(frequency[i] == i) return i;
    }

    return -1;
}