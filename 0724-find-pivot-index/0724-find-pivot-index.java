class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0 , lsum = 0 , pivot = -1;

        for( int i = 0 ; i < nums.length ; i++ ) sum += nums[i];

        for( int i = 0 ; i < nums.length ; i++){
            if( lsum == (sum - lsum - nums[i]) ){
                pivot = i;
                break;
            };
            lsum += nums[i];
        }
        return pivot;
    }
}