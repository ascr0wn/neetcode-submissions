class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level += 1
        return level