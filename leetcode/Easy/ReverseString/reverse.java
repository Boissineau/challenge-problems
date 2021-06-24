class Solution {
    public String reverseString(char[] s) {
        int i = 0;
        int j = s.length -1;
        double l1 = Math.floor(s.length/2);
        double l2 = Math.ceil(s.length/2);
        while(i <= l1 && j >= l2){
            if(i == j) break;
            char c = s[i];
            s[i] = s[j];
            s[j] = c;
            i += 1;
            j -= 1;
        }
        return String.copyValueOf(s);
    }
}




public class reverse {
    public static void main(String[] args){
        
        Solution sol = new Solution();
        char[] str = new char[]{'A',' ','m','a','n',',',' ','a',' ','p','l','a','n',',',' ','a',' ','c','a','n','a','l',':',' ','P','a','n','a','m','a'};
        String ret = sol.reverseString(str);
        System.out.println(ret);
    }

}
