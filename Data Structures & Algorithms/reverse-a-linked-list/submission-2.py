class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr != None:
            #tuple unpacking: first the right side is fully evaluated (left to right), made into a tuple than left side is assigned values
            curr.next, prev, curr = prev, curr, curr.next
        return prev