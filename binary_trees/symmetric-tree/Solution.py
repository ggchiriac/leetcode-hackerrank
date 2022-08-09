// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorder(self, root, arr):
        if root is None:
            arr.append(None)
            return
        arr.append(root.val)
        Solution.preorder(self, root.left, arr)
        Solution.preorder(self, root.right, arr)
        
    def inverseorder(self, root, arr):
        if root is None:
            arr.append(None)
            return
        arr.append(root.val)
        Solution.inverseorder(self, root.right, arr)
        Solution.inverseorder(self, root.left, arr)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        left = []
        right = []
        Solution.preorder(self, root.left, left)
        Solution.inverseorder(self, root.right, right)
        if len(left) != len(right):
            return False
        for i in range(len(left)):
            if left[i] != right[i]:
                return False
        return True