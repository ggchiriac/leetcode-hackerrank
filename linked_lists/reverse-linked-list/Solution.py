// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if head is None:
            return None
        nodes = []
        length = 0
        while node is not None:
            nodes.append(node)
            node = node.next
            length += 1
        for i in range(length - 1):
            nodes[length - i - 1].next = nodes[length - i - 2]
        nodes[0].next = None
        head = nodes[length - 1]
        return head
        
            
        