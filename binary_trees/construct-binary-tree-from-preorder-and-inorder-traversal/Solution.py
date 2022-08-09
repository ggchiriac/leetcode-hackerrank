// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(lIndex, rIndex):
            if lIndex > rIndex:
                return None
            
            value = preorder[0]
            preorder.remove(preorder[0])
            root = TreeNode(value)
            index = hashMap[root.val]
            
            root.left = helper(lIndex, index - 1)
            root.right = helper(index + 1, rIndex)
            return root
        
        hashMap = {value:index for index, value in enumerate(inorder)}
        return helper(0, len(inorder) - 1)