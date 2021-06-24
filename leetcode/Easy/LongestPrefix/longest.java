import java.util.ArrayList;

class Solution {
    public String longestCommonPrefix(String[] strs) {

        // Set<Character> s = new HashSet<>();
        ArrayList<Character> s = new ArrayList<>();
        ArrayList<Character> ret = new ArrayList<>();
        // Add all initial characters to the hashset
        for (char i : strs[0].toCharArray()){
            s.add(i);
        }
        
        // check all values of the next ones to see if they are in the strings

        for (int i = 1; i < strs.length; i++){
            for (int j = 0; j < strs[i].length(); j++){
                if (s.size() == 0) return "";
                if (strs[i].length() < s.size()){
                    for (int inc = strs[i].length(); inc < s.size(); inc += 0){
                        s.remove(inc);
                    }
                }


                char ch = strs[i].charAt(j);
                if (s.get(j) != ch){
                    for (int y = j; y < s.size(); y++){
                        if (s.size() == 0) return "";
                        s.remove(j);
                    }
                    break;
                }
            }

        }
        String sh = ""; 
        for(char i : ret){
            sh = sh + i;
        }

        return sh;
    }
}





public class longest {
    public static void main(String[] args){
        
        Solution sol = new Solution();
        String[] val = new String[]{"flower", "flow", "flight"};

        String ret = sol.longestCommonPrefix(val);
        System.out.println(ret);
    }

}
