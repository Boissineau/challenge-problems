class Solution(object):
    def isPowerOfTwo(self, n):
        
        
        def div(self, n):
            
            if n <= 0: return False 
            while(n % 2 == 0): n /= 2
            return n == 1
            
            if n <= 0: return False 
            return !(n & (n-1))
            
            if n == 1: return True 
            if n % 2 != 0 or n == 0: return False 
            return div(self, n/2)
            

        return div(self, n)