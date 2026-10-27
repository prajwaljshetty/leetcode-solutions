class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size() , left = 1 , right = 1;
        vector<int> answer(n , 1);

        for(int i = 0 ; i < n ; i++){
            answer[i] *= left;
            answer[n - i - 1] *= right;

            left *= nums[i];
            right *= nums[n - i - 1];
        }

        return answer;
    }
};