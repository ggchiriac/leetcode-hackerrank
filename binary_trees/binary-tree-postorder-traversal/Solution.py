// https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        pre = None
        stack, output = [], []
        
        while root is not None or stack:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if root.right is None or root.right is pre:
                    output.append(root.val)
                    stack.pop()
                    pre = root
                    root = None
                else:
                    root = root.right
            
        return output
                    
                
                
                
                