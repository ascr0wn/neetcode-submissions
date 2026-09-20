class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        def recursion(root):
            if not root:
                return []
            recursion(root.left)
            recursion(root.right)
            root.left, root.right = root.right, root.left
        
        recursion(root)
        return root

    