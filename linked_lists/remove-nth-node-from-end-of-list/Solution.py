// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node1 = head
        node2 = head
        prev = ListNode(0, head)
        p1 = 0
        
        if head == None or head.next == None:
            return None
        
        while node1 is not None:
            if p1 >= n:
                prev = node2
                node2 = node2.next
            p1 += 1
            node1 = node1.next

        if prev.next == head:
            return node2.next
        prev.next = node2.next
        
        return head