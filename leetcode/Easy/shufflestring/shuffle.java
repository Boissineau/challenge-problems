import java.util.ArrayList;

class Solution {
    public String restoreString(String s, int[] indices) {
        if(s.length() == 0) return "";
        char[] arr = new char[s.length()];
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            arr[indices[i]] = ch;
        }
        return String.valueOf(arr); 
    }
}



public class shuffle {
    public static void main(String[] args){
        
        Solution sol = new Solution();

        String str = "codeleet";
        int[] indices = new int[]{4,5,6,7,0,2,1,3};
        String ret = sol.restoreString(str, indices);
        System.out.println(ret);
    }

}
