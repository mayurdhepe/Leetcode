# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        n = len(arr)
        mid = n // 2
        
        newHead = ListNode()
        curr = newHead
        
        for i, n in enumerate(arr):
            if i != mid:
                curr.next = ListNode(n)
                curr = curr.next
                
        return newHead.next
        