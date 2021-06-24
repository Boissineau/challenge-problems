import java.util.Hashtable;

class Solution {
    public int fib(int n) {
        // if(n <= 2) return 1;
        // return fib(n-1) + fib(n-2);
        // ^^ is only thing needed to do a fib everything below was experimental 
        // with overloading methods to memoize
        Hashtable<Integer, Integer> hash = new Hashtable<>();
        int val = fib(n, hash);
        return val;  

    }

    public int fib(int n, Hashtable<Integer, Integer> hash) {
        if(hash.contains(n)){
            int val = hash.get(n);
            return val;
        }

        if (n <= 2) return 1;

        hash.put(n, fib(n-1, hash) + fib(n-2, hash));

        return hash.get(n);
    }


}





public class fib {
    public static void main(String[] args){
        
        Solution sol = new Solution();
        // char[] str = new char[]{'A',' ','m','a','n',',',' ','a',' ','p','l','a','n',',',' ','a',' ','c','a','n','a','l',':',' ','P','a','n','a','m','a'};
        int ret = sol.fib(10);
        System.out.println(ret);
    }

}
