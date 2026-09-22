# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        longest_path = 0

        def recursion(root):

            nonlocal longest_path

            if not root:
                return 0
            
            left_height = recursion(root.left)
            right_height = recursion(root.right)

            current_path = left_height + right_height
            if current_path > longest_path:
                longest_path = current_path
            
            return max(left_height, right_height) + 1

        recursion(root)

        return longest_path