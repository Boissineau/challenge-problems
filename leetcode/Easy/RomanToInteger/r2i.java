import java.util.Hashtable;

class Solution {
    public int romanToInt(String s) {
        
        Hashtable<Character, Integer> dict = new Hashtable<>();
        dict.put('I', 1);
        dict.put('V', 5);
        dict.put('X', 10);
        dict.put('L', 50);
        dict.put('C', 100);
        dict.put('D', 500);
        dict.put('M', 1000);
        
        int val = 0;
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            try {
                char next = s.charAt(i+1);
                if(dict.get(next) > dict.get(ch)){
                    int tmp = dict.get(next) - dict.get(ch);
                    val += tmp;
                    i += 1;
                    continue;
                }
                val += dict.get(ch);
                
            } catch (Exception e){
                val += dict.get(ch);
            }   
        }
        return val;
    }
}



public class r2i{


    public static void main(String[] args){

        Solution sol = new Solution();
        int ret = sol.romanToInt("MCMXCIV");
        System.out.println(ret);


    }
}