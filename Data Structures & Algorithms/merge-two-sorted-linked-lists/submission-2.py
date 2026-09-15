class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        p1 = list1
        p2 = list2
        temphead = list1
        while p1 and p2:
            if p1.val <= p2.val:
                while p1.next and p1.next.val <= p2.val:
                    p1 = p1.next
                temp = p2
                p2 = p2.next
                temp.next = p1.next
                p1.next = temp
                p1 = p1.next
            else:
                temp = p2.next
                p2.next = p1
                temphead = p2
                p1 = p2
                p2 = temp
        return list1 if list1.val < temphead.val else temphead