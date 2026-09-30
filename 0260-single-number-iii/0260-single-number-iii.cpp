class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xored = 0;
        for(int i = 0;i < nums.size() ; i++) xored ^= nums[i];

        int rightBit = 0;
        while(((xored >> rightBit) & 1) == 0) rightBit++;
    
        int setBit = 0 , unsetBit = 0;
        for(int i = 0;i < nums.size() ; i++){
            if(((nums[i] >> rightBit) & 1) == 0) setBit ^= nums[i];
            else unsetBit ^= nums[i];
        }

        return vector<int>{setBit,unsetBit};
    }
};