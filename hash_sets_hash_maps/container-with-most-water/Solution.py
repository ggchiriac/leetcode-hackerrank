// https://leetcode.com/problems/container-with-most-water

class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        aMax = min(height[l], height[r]) * (r - l)
        while l < r:
            aMax = max(aMax, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return aMax
            
            
        