class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        current = root
        depth = 0
        total_depth = 0
        while stack or current:
            while current:
                depth += 1
                stack.append([current,depth])
                current = current.left
                if depth > total_depth:
                    total_depth = depth
            current, depth = stack.pop()
            current = current.right
        return total_depth

