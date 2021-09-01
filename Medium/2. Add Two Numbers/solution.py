# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = None
        carry = 0
        
        while l1 is not None or l2 is not None:
            total_sum = carry
            
            if l1 is not None:
                total_sum += l1.val
                l1 = l1.next
                
            if l2 is not None:
                total_sum += l2.val
                l2 = l2.next
                
            node = ListNode(total_sum % 10)
            carry = total_sum // 10
            
            if temp is None:
                temp = head = node
            else:
                temp.next = node
                temp = temp.next
                
        if carry > 0:
            temp.next = ListNode(carry)
            
        return head