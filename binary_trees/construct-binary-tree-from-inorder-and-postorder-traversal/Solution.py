// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0], None, None)
        
        value = postorder[-1]
        index = inorder.index(value)
        lInorder = inorder[:index].copy()
        rInorder = inorder[(index + 1):].copy()
        lPostorder = []
        rPostorder = []
        
        if len(rInorder) != 0:
            split = rInorder[0]
            splitIndex = postorder.index(split)
            rPostorder = postorder[index:-1].copy()
            lPostorder = postorder[:index].copy()
        else:
            lPostorder = postorder[:-1].copy()
            
                
        node = TreeNode(value, None, None)
        node.left = Solution.buildTree(self, lInorder, lPostorder)
        node.right = Solution.buildTree(self, rInorder, rPostorder)
        
        return node  