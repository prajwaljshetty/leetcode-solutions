class Solution {
    public int singleNumber(int[] nums) {
        int bitIndex = 0 , bitCount = 0 , unique = 0;

        while (bitIndex < 32){
            bitCount = 0;
            for(int i = 0;i < nums.length;i++){
                if(((nums[i]>>bitIndex) & 1) == 1) bitCount++;
            }
            unique += (bitCount % 3 == 1 ? ( 1 << bitIndex ) : 0);
            bitIndex++;
        }
        return unique;
    }
}