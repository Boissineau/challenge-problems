import java.util.ArrayList;

class Solution {
    // public String defangIPaddr(String address) {
    //     String str = "";
    //     for(int i = 0; i < address.length(); i++){
    //         char ch = address.charAt(i);
    //         if (ch == '.'){
    //             str += "[.]";
    //         } else {
    //             str += ch;
    //         }
    //     }
    //     return str;
        
    // }

    public String defangIPaddr(String address) {
        return address.replace(".", "[.]");
    }
}




public class defang {
    public static void main(String[] args){
        
        Solution sol = new Solution();
        // char[] str = new char[]{'A',' ','m','a','n',',',' ','a',' ','p','l','a','n',',',' ','a',' ','c','a','n','a','l',':',' ','P','a','n','a','m','a'};
        String ret = sol.defangIPaddr("192.168.1.1");
        System.out.println(ret);
    }

}
