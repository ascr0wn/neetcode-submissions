class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        
        self.insert(val)

        return self.kthlargest()

    def kthlargest(self) -> int:
        temp = []
        for _ in range(self.k - 1):
            temp.append(self.deleteTop())
        kthlargest_value = self.nums[0]
        for num in temp:
            self.insert(num)
        return kthlargest_value

    def insert(self, val:int):
        self.nums.append(val)
        self.bubbleUp()

    def bubbleUp(self):
        current_index = len(self.nums) - 1
        current_parent = (current_index - 1) // 2
        
        while self.nums[current_parent] <= self.nums[current_index] and current_index > 0:
            self.nums[current_index], self.nums[current_parent] = self.nums[current_parent], self.nums[current_index]
            current_index = current_parent
            current_parent = (current_index - 1) // 2
    
    def deleteTop(self) -> int:
        top = self.nums[0]
        self.nums[0] = self.nums.pop()
        self.bubbleDown()
        return top
            
    def bubbleDown(self):
        total_index = len(self.nums) - 1
        current_index = 0
        left_child_index = current_index * 2 + 1
        right_child_index = current_index * 2 + 2
        if left_child_index > total_index and right_child_index > total_index:
            return
        if left_child_index > total_index:
            bigger_child_index = right_child_index
        elif right_child_index > total_index:
            bigger_child_index = left_child_index
        else:
            bigger_child_index = left_child_index if self.nums[left_child_index] >= self.nums[right_child_index] else right_child_index 
        while self.nums[bigger_child_index] >= self.nums[current_index]:
            self.nums[bigger_child_index], self.nums[current_index] = self.nums[current_index], self.nums[bigger_child_index]
            current_index = bigger_child_index
            left_child_index = current_index * 2 + 1
            right_child_index = current_index * 2 + 2
            if left_child_index > total_index and right_child_index > total_index:
                return
            if left_child_index > total_index:
                bigger_child_index = right_child_index
            elif right_child_index > total_index:
                bigger_child_index = left_child_index
            else:
                bigger_child_index = left_child_index if self.nums[left_child_index] >= self.nums[right_child_index] else right_child_index