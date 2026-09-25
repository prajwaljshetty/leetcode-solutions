class Solution {
    static int sum(int n){
        if( n == 0 ) return 0;
        return n % 10 + sum( n / 10);
    }
    public int smallestIndex(int[] nums) {
        int i = 0;
        while(i < nums.length){
            if(sum(nums[i]) == i ) return i;
            i++;
        }
        return -1;
    }
}