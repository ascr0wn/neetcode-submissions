class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        depth = 0
        max_depth = 0
        while root or stack:
            while root:
                depth += 1
                stack.append((root,depth))
                root = root.left
                max_depth = depth if depth > max_depth else max_depth
            root,depth = stack.pop()
            root = root.right
        return max_depth