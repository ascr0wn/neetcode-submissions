#Proper recursive
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recursive(root):
            if not root:
                return [True,0]
            left,right = recursive(root.left), recursive(root.right)
            balenced = left[0] and right[0] and abs(left[1]-right[1])<2
            return [balenced, 1 + max(left[1],right[1])]
    
        return recursive(root)[0]