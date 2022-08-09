// https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hset1 = set()
        hset2 = set()
        for x in nums1:
            if x not in hset1:
                hset1.add(x)
        for x in nums2:
            if x in hset1 and x not in hset2:
                hset2.add(x)
        return [x for x in hset2]
        