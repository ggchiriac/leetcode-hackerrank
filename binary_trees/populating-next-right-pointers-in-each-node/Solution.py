// https://leetcode.com/problems/populating-next-right-pointers-in-each-node

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def bfs(root: 'Node'):
            if root is None:
                return
            queue = [root]
            i = 1
            k = 0
            past_node = Node()

            while len(queue) > 0:
                cur_node = queue.pop(0)
                past_node.next = cur_node
                if i == 2**k + 1:
                    k += 1
                    past_node.next = None
                    i = 1
                past_node = cur_node
                i += 1

                if cur_node.left is not None:
                    queue.append(cur_node.left)

                if cur_node.right is not None:
                    queue.append(cur_node.right)
                    
        bfs(root)
        return root