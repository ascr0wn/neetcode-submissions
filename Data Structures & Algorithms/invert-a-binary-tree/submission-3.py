class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        if not root:
            return root
        queue = [root]
        delete = 0
        insert = 1        
        while delete != insert:
            if queue[delete]:
                node = queue[delete]
                delete += 1
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
                insert += 1
            if node.right:
                queue.append(node.right)
                insert += 1
        return root