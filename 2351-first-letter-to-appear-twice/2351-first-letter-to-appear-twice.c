char repeatedCharacter(char* s) {
    int freq[26] = {0};

    for(int i = 0 ; s[i] != '\0' ; i++){
        if(freq[s[i] - 'a'] == -1) return s[i];
        freq[s[i] - 'a'] -= 1;
    }

    return 'f';
}