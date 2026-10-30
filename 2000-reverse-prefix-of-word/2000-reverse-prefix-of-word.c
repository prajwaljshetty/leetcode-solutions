char* reversePrefix(char* word, char ch) {
    int pos = 0;

    while(word[pos] != '\0' && word[pos] != ch) pos++;

    if(word[pos] == '\0') return word;

    int mid = (pos)/ 2;
    char temp;

    for(int i = 0 ; i <= mid ; i++){
        temp = word[i];
        word[i] = word[pos - i];
        word[pos - i] = temp;
    }

    return word;
}