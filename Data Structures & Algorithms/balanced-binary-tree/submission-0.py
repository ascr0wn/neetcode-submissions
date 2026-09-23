# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def recursion(root):
            
            if not root:
                return 0

            left_height = recursion(root.left)
            right_height = recursion(root.right)

            if left_height == -1 or right_height == -1:
                return -1

            if abs(left_height - right_height) >= 2:
                return -1
            else:
                return max(left_height, right_height) + 1
            
        if recursion(root) == -1:
            return False 
        else:
            return True
    

