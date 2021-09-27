# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        prevNode = ListNode(0) 
        prevNode.next = head
        
        prev = prevNode
        temp = head
        
        while temp!=None:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = prev.next
                
            temp = temp.next
            
        return prevNode.next