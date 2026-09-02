# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 1
        while curr.next:
            curr = curr.next
            count += 1
        
        now = head
        if n == count:
            return head.next
        for _ in range((count-n)-1):
            now = now.next
        
        now.next = now.next.next
        return head