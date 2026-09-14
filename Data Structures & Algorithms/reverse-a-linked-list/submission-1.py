class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head

        previous = None
        current = head

        def recursion(previous, current):
            if current.next == None:
                current.next = previous
                head = current
                return head
            else:
                head = recursion(current, current.next)
                current.next = previous
                return head
        return recursion(previous, current)