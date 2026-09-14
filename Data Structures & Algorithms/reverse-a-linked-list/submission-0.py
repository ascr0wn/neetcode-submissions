class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        previous = None
        current = head
        next = head.next
        while True:
            current.next = previous
            previous = current
            current = next
            if current == None:
                break    
            next = current.next
        head = previous
        return head