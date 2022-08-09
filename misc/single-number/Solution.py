// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hset = set()
        for x in nums:
            if x in hset:
                hset.remove(x)
            else:
                hset.add(x)
        for x in hset:
            return x