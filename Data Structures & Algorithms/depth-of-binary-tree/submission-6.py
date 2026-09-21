class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        level = 1
        queue.append((root,1))
        while queue:
            current, level = queue.popleft()
            if current.left:
                queue.append((current.left, level+1))
            if current.right:
                queue.append((current.right, level+1))
        return level
