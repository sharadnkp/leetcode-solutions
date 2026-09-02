# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        
        if length == n:
            return head.next
        
        position = length - n
        count = 1
        curr = head
        while count < position:
            curr = curr.next
            count += 1
        
        curr.next = curr.next.next
        return head
        
