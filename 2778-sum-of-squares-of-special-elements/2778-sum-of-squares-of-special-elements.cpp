class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        int SOS = 0;


        for(int i = 0 ; i < nums.size() ; i++){
            SOS += ((nums.size() % (i + 1)) == 0) ? (nums[i] * nums[i]) : 0;
            cout << SOS << "\n";
        }

        return SOS;
    }
};