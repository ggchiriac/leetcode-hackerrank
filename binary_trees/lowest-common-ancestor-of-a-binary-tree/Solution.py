// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse(node: 'TreeNode', path: List):
            nonlocal pathP
            nonlocal pathQ 
            
            if node == p:
                pathP = path + [node]
            elif node == q:
                pathQ = path + [node]
            if node.left is None and node.right is None:
                return

            if node.left is not None:
                recurse(node.left, path + [node])
                
            if node.right is not None:    
                recurse(node.right, path + [node])
          
        pathP = []
        pathQ = []
        recurse(root, [])
        setQ = set(pathQ)
        for i in range(len(pathP) - 1, -1, -1):
            if pathP[i] in setQ:
                return pathP[i]
                
        