package Easy.TwoSum;
import java.util.Arrays;


class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] indices = new int[2];
        for (int i = 0; i < nums.length; i++){
            for (int j = 0; j < nums.length; j++){
                if (i == j){
                    continue;
                }
                if((nums[i] + nums[j]) == target){
                    indices[0] = i;
                    indices[1] = j;
                }
            }
        }
        
        return indices;
    }
}

class TwoSum {

    public static void main(String[] args){
    
        Solution sol = new Solution();
        int[] arr = new int[]{1,2,3,4,5};
        int[] indices = sol.twoSum(arr, 4);
        System.out.println(Arrays.toString(indices));
    
    }
}