# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        rev = l[::-1]
        
        return True if l == rev else False 
        
# https://leetcode.com/problems/palindrome-linked-list/submissions/