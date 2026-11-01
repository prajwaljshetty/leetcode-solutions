class Solution {
public:
    bool check(vector<int>& nums) {
        int left = 0;

        for(left = 0 ; left < nums.size() - 1 && nums[left] <= nums[left + 1]; left++);

        if(left == nums.size()) return true;

        for(int i = left + 1 ; i < (nums.size() + left ) ; i++){
            int j = i % nums.size();
            if(nums[j] > nums[(j + 1) % nums.size()]) return false;
        }

        return true;
    }
};

