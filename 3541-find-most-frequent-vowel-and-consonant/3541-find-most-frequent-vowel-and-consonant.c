int maxFreqSum(char* s) {
    int frequency [26] = {0};

    for(int i = 0 ; s[i] != '\0' ; i++){
        frequency[s[i] - 'a'] += 1;
    }

    int vMax = 0 , cMax = 0;

    for(int i = 0 ; i < 26 ; i++){
        char c = i + 'a';
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') 
            vMax = frequency[i] > vMax ? frequency[i] : vMax;
        else
            cMax = frequency[i] > cMax ? frequency[i] : cMax;
    }

    return vMax + cMax;
}