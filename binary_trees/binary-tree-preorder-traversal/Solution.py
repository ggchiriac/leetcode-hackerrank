// https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# Recursive:
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#         if root.left is None and root.right is None:
#             return [root.val]
#         else:
#             return [root.val] + Solution.preorderTraversal(self, root.left) + Solution.preorderTraversal(self, root.right)
#
# Iterative:
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        nodes = []
        node = root
        prev = TreeNode(0, root, None)
        ok = 0
        while ok is 0 and node is not None:
            ok = 1
            prev = root
            node = root
            if node not in nodes:
                nodes.append(node)
                values.append(node.val)
                ok = 0
            while node.left is not None or node.right is not None:
                if node.left is not None:
                    prev = node
                    node = node.left
                    if node not in nodes:
                        nodes.append(node)
                        values.append(node.val)
                        ok = 0
                elif node.right is not None:
                    prev = node
                    node = node.right
                    if node not in nodes:
                        nodes.append(node)
                        values.append(node.val)
                        ok = 0
            if node == prev.left:
                prev.left = None
                ok = 0
            elif node == prev.right:
                prev.right = None
                ok = 0
        return values