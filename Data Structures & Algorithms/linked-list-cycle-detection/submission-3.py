class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_dict = {}
        my_array = [[] for _ in range(2001)]
        pointer = head
        while pointer:
            if pointer.val in my_dict:
                if my_dict[pointer.val] == pointer:
                    return True
                else:
                    for array_val in my_array[pointer.val + 1000]:
                        if array_val == pointer:
                            return True
                    my_array[pointer.val + 1000].append(pointer)
            my_dict[pointer.val] = pointer
            pointer = pointer.next
        return False