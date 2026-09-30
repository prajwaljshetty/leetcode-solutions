class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xored = 0;
        for(int i = 0;i < nums.size() ; i++) xored ^= nums[i];

        int rightBit = 0;
        while(((xored >> rightBit) & 1) == 0) rightBit++;
    
        int unique1 = 0 , unique2 = 0;
        for(int i = 0;i < nums.size() ; i++){
            if(((nums[i] >> rightBit) & 1) == 0) unique1 ^= nums[i];
            else unique2 ^= nums[i];
        }

        return vector<int>{unique1,unique2};
    }
};