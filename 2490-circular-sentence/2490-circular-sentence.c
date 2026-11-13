bool isCircularSentence(char* sentence) {
    char prev = '\0';

    for(int i = 1 ; sentence[i] != '\0' ; i++){
        if(sentence[i] == ' '){
            prev = sentence[i - 1];
        }else if(sentence[i - 1] == ' '){
            if(prev != sentence[i]) return false;
        }
    }

    return sentence[0] == sentence[ strlen(sentence) - 1];
}