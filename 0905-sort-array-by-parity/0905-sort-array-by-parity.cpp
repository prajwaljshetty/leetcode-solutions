class Solution {
public:
    void swap( int *x , int *y ){
        int temp = *x;
        *x = *y;
        *y =temp;
    }
    vector<int> sortArrayByParity(vector<int>& nums) {
        int left = 0 , right = nums.size() - 1;

        while(left < right){
            if((nums[left] % 2) == 1) 
                swap(&nums[left],&nums[right--]);
            else
                left++;
        }

        return nums;
    }
};