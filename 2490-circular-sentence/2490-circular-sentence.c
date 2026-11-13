bool isCircularSentence(char* sentence) {

    for(int i = 0 ; sentence[i + 1] != '\0' ; i++){
        if(sentence[i] == ' '){
            if(sentence[i - 1] != sentence[i + 1]) return false;
        }
    }

    return sentence[0] == sentence[ strlen(sentence) - 1];
}