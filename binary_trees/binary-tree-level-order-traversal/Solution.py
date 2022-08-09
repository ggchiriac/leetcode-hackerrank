// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        queue, output = [root], [[root.val]]
        level = []
        count1 = 1
        count2 = 0
        while queue:
            root = queue.pop(0)
            count1 -= 1
            if root.left is not None:
                level.append(root.left.val)
                queue.append(root.left)
                count2 += 1
            if root.right is not None:
                level.append(root.right.val)
                queue.append(root.right)
                count2 += 1
            if count1 is 0:
                count1 = count2
                count2 = 0
                if level:
                    output.append(level)
                level = []
        return output
            
            
        