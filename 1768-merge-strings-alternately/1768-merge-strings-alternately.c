

char * mergeAlternately(char * word1, char * word2){
    int length1 = strlen(word1) , length2 = strlen(word2);

    char* merged = malloc((length1+ length2) * sizeof(int));

    int i = 0 , j = 0 , k = 0 ;

    while( i < length1 && j < length2){
        if(k % 2 == 0){
            merged[k++] = word1[i++];
        }else{
            merged[k++] = word2[j++];
        }
    }

    while(i < length1) merged[k++] = word1[i++];

    while(j < length2) merged[k++] = word2[j++];

    merged[length1 + length2 ] = '\0';
    return merged;
}