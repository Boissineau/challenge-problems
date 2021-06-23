

class Solution {
    public int maxSubArray(int[] nums) {
        int tmp = 0;
        int sum = nums[0];

        for(int i = 0; i < nums.length; i++){
            for(int j = i; j < nums.length; j++){
                tmp += nums[j];
                if (tmp > sum) sum = tmp;
            }
            tmp = 0;
        }
        return sum;
    }
}





public class maxsum {
    public static void main(String[] args){
        
        Solution sol = new Solution();
        int[] arr = new int[]{-2,1,-3,4,-1,2,1,-5,4};
        int sum = sol.maxSubArray(arr);
        System.out.println(sum);
    }

}


// -2,1,-3,4,-1,2,1,-5,4
//  ^ ^ 