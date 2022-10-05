# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        dummy2 = head
        length = 1
        
        while dummy.next != None:
            length += 1
            dummy = dummy.next
        
        if length == n:
            head = head.next
            return head
            
        for i in range(1, (length-n)):
            dummy2 = dummy2.next
        dummy2.next = dummy2.next.next
        return head