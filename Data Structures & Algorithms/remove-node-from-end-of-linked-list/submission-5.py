# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        if not head.next:
            return None
        else:
            count = 0
            trail, ptr = dummy, dummy
            while count <= n:
                ptr = ptr.next
                count += 1
            while ptr:
                trail = trail.next
                ptr = ptr.next
            
            trail.next = trail.next.next if trail.next else None
        return dummy.next