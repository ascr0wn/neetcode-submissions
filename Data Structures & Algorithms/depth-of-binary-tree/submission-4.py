class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.maxDepth(root.left) + 1
        right_height = self.maxDepth(root.right) + 1
        return max(left_height, right_height)