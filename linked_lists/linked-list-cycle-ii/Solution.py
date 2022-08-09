// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cur = head
        if cur is None: return None
        nodes = []
        nodes.append(cur)
        while cur is not None:
            cur = cur.next
            if cur is None: return None
            for node in nodes:
                if node is cur: return cur
            nodes.append(cur)
            
        return None
        