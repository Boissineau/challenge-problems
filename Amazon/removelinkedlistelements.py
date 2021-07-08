# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
#         node = head 
#         while(node and node.next):
#             if node.next.val != val:
#                 node = node.next 
#                 continue 
#             node.next = node.next.next 
#         if head and head.val == val:
#             if head.next: return head.next
#             return None
            

        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return dummy.next