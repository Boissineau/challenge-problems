


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        
        result = ListNode()
        result_tail = result 
        carry = 0 

        
        while l1 or l2 or carry:
            x = l1.val if l1 else 0 
            y = l2.val if l2 else 0
            sum = carry + x + y 
            carry = sum // 10
            val = sum % 10
            
            result_tail.next = ListNode(val) 
            result_tail = result_tail.next 
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
        
        
        return result.next 


# https://leetcode.com/problems/add-two-numbers/submissions/