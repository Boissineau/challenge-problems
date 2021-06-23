import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;


class Solution {
    public int lengthOfLongestSubstring(String s) {

        if (s.length() == 1) return 1;
        
    
        ArrayList<Character> ch_set = new ArrayList<>();

        int len = 0;
        int tmp = 0;
        for (int i = 0; i < s.length(); i++){

            char ch = s.charAt(i);

            if(ch_set.contains(ch)){
                int idx = ch_set.indexOf(ch);
                for (int j = 0; j <= idx; j++){
                    ch_set.remove(0);                    
                }
                ch_set.add(ch);
                if (tmp > len) len = tmp;
                tmp = ch_set.size();

            } else {
                ch_set.add(ch);
                tmp += 1;
            }
        }
        
        if (tmp > len) return tmp; else return len;
    }
}



public class longest {
    public static void main(String[] args){
        Solution sol = new Solution();
        int rev = sol.lengthOfLongestSubstring("aabaab!bb");
        System.out.println(rev);
    }

}