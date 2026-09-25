class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
       int[] frequency = new int[1001];        
       for( int i = 0 ; i < nums1.length ; i++ ) frequency[nums1[i]]++ ;

        int curIndex = 0;
        for(int i = 0 ; i < nums2.length ; i++){
            if(frequency[nums2[i]] > 0 ){
                nums1[curIndex++] = nums2[i];
                frequency[nums2[i]]--;
            }
        }
        
        return Arrays.copyOf(nums1 ,  curIndex);
    }
}