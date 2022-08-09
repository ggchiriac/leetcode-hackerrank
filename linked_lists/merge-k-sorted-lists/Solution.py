// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        start = None
        min = math.inf
        iMin = -1
        ok = 0
        for i in range(len(lists)):
            if lists[i] is not None:
                ok = 1
                if lists[i].val < min:
                    min = lists[i].val
                    iMin = i
        if ok == 1:
            start = lists[iMin]
            lists[iMin] = lists[iMin].next
            cur = start
        while True:
            ok = 0
            min = math.inf
            iMin = -1
            for i in range(len(lists)):
                if lists[i] is not None:
                    ok = 1
                    if lists[i].val < min:
                        min = lists[i].val
                        iMin = i
            if ok == 0:
                break
            cur.next = lists[iMin]
            cur = cur.next
            lists[iMin] = lists[iMin].next
            if lists[iMin] is None:
                lists.pop(iMin)
        return start