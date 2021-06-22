class Solution:
    def reverseList(self, head):
        curr = head 
        previous = None 

        while True:
            if curr is None:
                break
            tmp_curr = curr.next 
            curr.next = previous
            previous = curr
            if tmp_curr is None:
                break
            curr = tmp_curr


        return curr

        



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



if __name__ == '__main__':

    node = ListNode(0);
    head = node
    for i in range(1,10):
        node.next = ListNode(i)
        node = node.next

    x = Solution()
    v = x.reverseList(head)
    for i in range(10):
        print(v.val)
        v = v.next
