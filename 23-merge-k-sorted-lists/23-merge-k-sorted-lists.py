# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = result = ListNode(0)
        res = []
        
        for lis in lists:
            while lis != None:
                res.append(lis.val)
                lis = lis.next
        heapq.heapify(res)
        
        while res:
            newNode = ListNode(heapq.heappop(res))
            result.next = newNode
            result = newNode
        
        return dummy.next