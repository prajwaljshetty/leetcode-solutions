int findPermutationDifference(char* s, char* t) {
    int alphaMap[26] , absoluteDifference = 0;

    for(int i = 0 ; s[i] != '\0' ; i++){
        alphaMap[s[i] - 'a'] = i;
    }

    for(int i = 0 ;  t[i] != '\0' ; i++){
        absoluteDifference += abs( i - alphaMap[t[i] - 'a']);
    }

    return absoluteDifference;
}