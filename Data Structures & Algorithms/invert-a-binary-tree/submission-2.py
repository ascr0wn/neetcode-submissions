class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        def recursive(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            recursive(root.left)
            recursive(root.right)
        recursive(root)
        return root