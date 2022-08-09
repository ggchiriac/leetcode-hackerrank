// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            elif abs(i - hashMap[nums[i]]) <= k:
                return True
            else:
                hashMap[nums[i]] = i
        return False
        