# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recursion(root, depth):
            if not root:
                return depth
            left = recursion(root.left, depth) + 1
            right = recursion(root.right, depth) + 1
            return left if left > right else right
        
        return recursion(root, 0)