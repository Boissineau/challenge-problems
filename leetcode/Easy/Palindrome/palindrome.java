import java.util.ArrayList;

class Solution {
    public boolean isPalindrome(int x) {
        
        if (x < 0) return false;

        String s = String.valueOf(x);
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            int val = Character.getNumericValue(ch);
            arr.add(val);
        }

        int val = 0;
        double length = s.length();
        double floor = Math.floor(length/2);
        double ciel = Math.ceil(length/2);

        int i = 0;
        int j = s.length() - 1;

        while(i < floor && j >= ciel){
            if (val != 0) return false;
            val += arr.get(i);
            val -= arr.get(j);
            i += 1;
            j-= 1;
        }
    
        
        if (val == 0) return true;
        return false;

        

        
        
        
    }
}


public class palindrome {
    public static void main(String[] args){
        
        Solution sol = new Solution();
        boolean ret = sol.isPalindrome(12221);
        System.out.println(ret);
    }

}
