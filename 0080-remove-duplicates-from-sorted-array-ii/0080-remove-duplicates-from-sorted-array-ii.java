class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 1 , writeIndex = 1 ;
        for(int i = 1 ; i < nums.length ; i++ ){
            if(nums[i] == nums[i-1]){
              if( count < 2){
                count++;
                nums[writeIndex] = nums[i];
                writeIndex++;
              }
            }else{
                nums[writeIndex++] = nums[i];
                count = 1;
            }
        }

        return writeIndex;
    }

}