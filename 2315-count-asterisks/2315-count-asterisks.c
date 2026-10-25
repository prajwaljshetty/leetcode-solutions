int countAsterisks(char* s) {
    bool flag = true;
    int count = 0;

    for(int i = 0 ; s[i] != '\0' ; i++){
        if(s[i] == '|') flag = !flag;
        if(flag && s[i] == '*') count++;
    }

    return count;
}