class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        if not root:
            return None
        bft = []
        bft.append(root)
        for node in bft:
            if node.left:
                bft.append(node.left)
            if node.right:
                bft.append(node.right)
        for node in bft:
            node.left, node.right = node.right, node.left
        return root