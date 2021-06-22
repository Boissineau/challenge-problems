class Solution {
    public int reverse(int x) {
        try {
            boolean sign = false;
            if (x < 0) sign = true;

            String str = new String();
            StringBuilder str2 = new StringBuilder();
            str = String.valueOf(Math.abs(x));
            str2.append(str);
            str2.reverse();
            if (sign) str2.insert(0, "-");

            int ret = Integer.parseInt(str2.toString());

            return ret;
            
        } catch (Exception e){
            return 0;
        }
    }

    public int reverse2(int x){

        

        return 1;


    }
}




public class ReverseInteger {
    public static void main(String[] args){
        Solution sol = new Solution();
        int rev = sol.reverse(-19248);
        System.out.println(rev);
    }

}