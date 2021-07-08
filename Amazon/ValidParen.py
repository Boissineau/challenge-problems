# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False 
        if s[0] == ')' or s[0] == '}' or s[0] == ']': return False
        pairs = {')' : '(',
                 ']' : '[', 
                 '}' : '{'}
        
        l = [] 
        for i in s: 
            if (i == ')' or i == ']' or i == '}') and len(l) != 0:
                if l[-1] == pairs[i]:
                    l.pop() 
                    continue
                else:
                    return False 
                
            l.append(i) 
        
        if len(l) > 0: return False
        return True