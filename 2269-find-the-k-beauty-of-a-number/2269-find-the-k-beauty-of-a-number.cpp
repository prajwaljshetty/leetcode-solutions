class Solution {
public:
    int divisorSubstrings(int num, int k) {
    vector<int> digits;
    int temp = num , count = 0;

    while(temp > 0){
        digits.push_back(temp % 10);
        temp /= 10;
    }

    for(int i = digits.size() - 1 ; i >= k - 1 ; i--){
        int substring  = 0;
        for(int j = 0 ; j < k ; j++){
            substring = (substring * 10) + digits[i - j];
        }
        if((substring > 0) && (num % substring) == 0) count++;
    }

    return count;
    
    }
};