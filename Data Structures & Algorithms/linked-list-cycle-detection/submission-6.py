# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        slow_pointer = head
        fast_pointer = head.next
        while slow_pointer != fast_pointer:
            if not slow_pointer.next:
                return False
            if not fast_pointer.next:
                return False
            if not fast_pointer.next.next:
                return False
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return True