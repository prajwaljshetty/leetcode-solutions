char* restoreString(char* s, int* indices, int indicesSize) {
    char *shuffle = malloc(indicesSize + 1);

    for(int i = 0 ; i < indicesSize ; i++){
        shuffle[indices[i]] = s[i];
    }

    shuffle[indicesSize] = '\0';

    return shuffle;
}