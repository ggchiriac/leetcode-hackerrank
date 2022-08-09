// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        oddtail = head
        eventail = head.next
        dummy = head.next
        while eventail is not None:
            odd = eventail.next
            oddtail.next = odd
            if odd is None:
                oddtail.next = dummy
                break
            eventail.next = odd.next
            odd.next = dummy
            eventail = eventail.next
            oddtail = odd
        return head
            
            