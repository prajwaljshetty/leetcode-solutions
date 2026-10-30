class Solution {
public:
    int pivotInteger(int n) {
        for(int i = 1 ; i < n + 1 ; i++){
            if(((i * (i + 1)) / 2) == (((n - i + 1) * (i + n)) / 2)) return i;
        }

        return -1;
    }
};