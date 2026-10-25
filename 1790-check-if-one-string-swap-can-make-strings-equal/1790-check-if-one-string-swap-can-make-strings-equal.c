void swap(char* x , char* y){
    char temp = *x;
    *x = *y;
    *y = temp;
}

bool areAlmostEqual(char* s1, char* s2) {
    if(strlen(s1) != strlen(s2)) return false;
    int mismatchIndex = -1;

   for(int i = 0 ; i < strlen(s2) ; i++){
        if(s1[i] != s2[i]){
            if( mismatchIndex != -1){
                swap(&s2[mismatchIndex] , &s2[i]);
                if((strcmp(s1 , s2)) == 0){
                    return true;
                }else{
                    return false;
                }
            }else{
               mismatchIndex = i;
            }
        }
   }
   return (strcmp(s1 , s2)) == 0;
}