class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 3 or n == 1: return True 
        if n < 3 or n%3 != 0: return False 
        
        return self.isPowerOfThree(n/3)
        
    
# https://leetcode.com/problems/power-of-three/submissions/