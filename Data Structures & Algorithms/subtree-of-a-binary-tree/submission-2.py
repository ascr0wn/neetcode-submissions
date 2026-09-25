# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        sub_root_value = subRoot.val
        stack = [root]

        def dfs(root) -> bool:
            
            nonlocal stack
            nonlocal sub_root_value

            while stack:
                current = stack.pop()
                if current.val == sub_root_value:        
                    if isSimilar(current, subRoot):
                        return True
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
            return False    

        def isSimilar(root, subRoot) -> bool:
            stack2 = [(root,subRoot)]
            while stack2:
                current1, current2 = stack2.pop()
                if not current1 and not current2:
                    continue
                if not current1 or not current2 or current1.val != current2.val:
                    return False
                stack2.append((current1.left, current2.left))
                stack2.append((current1.right, current2.right))
            return True

        flag = dfs(root)
        return flag