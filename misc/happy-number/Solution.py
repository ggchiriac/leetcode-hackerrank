// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        hset = set()
        while n != 1 and n not in hset:
            hset.add(n)
            nCopy = 0
            while n >= 1:
                nCopy += (int(n) % 10)**2
                n = int(int(n) / 10)
            n = nCopy
        if n == 1:
            return True
        return False