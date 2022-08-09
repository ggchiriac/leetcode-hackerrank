// https://leetcode.com/problems/count-univalue-subtrees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isUnival(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.right is None:
            return (root.val == root.left.val
                   and Solution.isUnival(self, root.left)
                   and Solution.isUnival(self, root.right))
        if root.left is None:
            return (root.val == root.right.val
                    and Solution.isUnival(self, root.left)
                    and Solution.isUnival(self, root.right))   
        return (root.val == root.left.val
                and root.val == root.right.val
                and Solution.isUnival(self, root.left)
                and Solution.isUnival(self, root.right))
        
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0;
        if root.left is None and root.right is None:
            return 1;
        current = 0
        if Solution.isUnival(self, root):
            current = 1
        return current + Solution.countUnivalSubtrees(self, root.left) + Solution.countUnivalSubtrees(self, root.right)