int contains(char *word, char key[]) {
    int wordLength = strlen(word);
    int keyLength = strlen(key);

    if (keyLength > wordLength) return -1;
    if (keyLength == 0) return 0;

    for (int i = 0; i <= wordLength - keyLength; i++) {
        if (word[i] == key[0]) {
            int j;
            for (j = 0; j < keyLength; j++) {
                if (word[i + j] != key[j]) break;
            }
            if (j == keyLength) return i;
        }
    }
    return -1;
}

char *replace(char *word, char old[], int start, char new[]) {
    int wordLength = strlen(word);
    int oldLength = strlen(old);
    int newLength = strlen(new);

    int resultLength = wordLength - oldLength + newLength + 1;
    char *result = malloc(resultLength);

    if (result == NULL) return NULL;

    for (int i = 0; i < start; i++) {
        result[i] = word[i];
    }

    for (int i = 0; i < newLength; i++) {
        result[start + i] = new[i];
    }

    for (int i = start + oldLength; i < wordLength; i++) {
        result[start + newLength + i - (start + oldLength)] = word[i];
    }

    result[resultLength - 1] = '\0';
    return result;
}

char *interpret(char *command) {
    char *result = malloc(strlen(command) + 1) ,  *temp;

    if (result == NULL) return NULL;

    strcpy(result, command);

    int start;

    while ((start = contains(result, "()")) != -1) {
        temp = result;
        result = replace(result, "()", start, "o");
        free(temp);
    }

    while ((start = contains(result, "(al)")) != -1) {
        temp = result;
        result = replace(result, "(al)", start, "al");
        free(temp);
    }

    return result;
}