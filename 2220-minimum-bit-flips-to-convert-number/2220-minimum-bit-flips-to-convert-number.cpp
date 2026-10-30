class Solution {
public:
    int minBitFlips(int start, int goal) {
        int i = 0 , count = 0;

        int max = start > goal ? start : goal;

        while((max >> i) > 0){
            if(((start >> i) & 1 ) != ((goal >> i) & 1)) count++;
            i++;
        }
        
        return count;
    }
};