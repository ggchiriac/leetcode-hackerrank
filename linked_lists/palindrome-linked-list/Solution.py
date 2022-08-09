// https://leetcode.com/problems/palindrome-linked-list

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = 0
        node = ListNode(0 , head)
        while node.next is not None:
            node = node.next
            l += 1
        c = 1
        curhead = head
        if l < 2: 
            return True
        if l == 2:
            if head.val == head.next.val: 
                return True;
            else:
                return False
        while c < int(l / 2):
            c += 1
            p = head.next
            head.next = p.next
            p.next = curhead
            curhead = p
        head = head.next
        if l % 2 == 1:
            head = head.next
        while head is not None:
            if head.val != curhead.val: return False
            head = head.next
            curhead = curhead.next
        return True