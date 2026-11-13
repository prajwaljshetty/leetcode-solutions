int prefixCount(char** words, int wordsSize, char* pref) {
    int count = 0;

    for(int i = 0 ; i < wordsSize ; i++){
        int x = 0;
        while(pref[x] != '\0' && words[i][x] == pref[x]) x++;
        if (x == strlen(pref)) count++;
    }

    return count;
}