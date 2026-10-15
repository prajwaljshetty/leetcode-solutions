char nextGreatestLetter(char* letters, int lettersSize, char target) {
    int key = target , min = 'z' + 1;

    for(int i = 0 ; i < lettersSize ; i++ ){
        if( letters[i] > key && letters[i] < min ) min = letters[i];
    }

    return min == 'z' + 1 ? letters[0] : min;
}