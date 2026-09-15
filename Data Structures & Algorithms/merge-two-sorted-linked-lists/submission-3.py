# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        p1 = list1
        p2 = list2

        while p1 and p2:
            newnode = ListNode(val=p2.val)
            if p2.val >= p1.val:
                while p1.next and p1.next.val <= p2.val:
                    p1 = p1.next
                newnode.next = p1.next
                p1.next = newnode
                p1 = p1.next
                p2 = p2.next
            else:
                newnode.next = p1
                list1 = newnode
                p1 = newnode
                p2 = p2.next

        return list1

