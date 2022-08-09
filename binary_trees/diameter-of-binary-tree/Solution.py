// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxPath(node: Optional[TreeNode]) -> int:
            nonlocal lMax
            if node.left is None and node.right is None:
                return 0
            if node.left is not None:
                leftGain = 1 + maxPath(node.left)
            else:
                leftGain = 0
            if node.right is not None:
                rightGain = 1 + maxPath(node.right)
            else:
                rightGain = 0
            lMax = max(lMax, leftGain + rightGain)
            return max(leftGain, rightGain)
            
        lMax = 0
        maxPath(root)
        return lMax
            
        