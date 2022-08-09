// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMaps = {}
        for i, char in enumerate(s):
            if char not in hashMaps:
                hashMaps[char] = t[i]
            else:
                if hashMaps[char] != t[i]:
                    return False
        hashMapt = {}
        for i, char in enumerate(t):
            if char not in hashMapt:
                hashMapt[char] = s[i]
            else:
                if hashMapt[char] != s[i]:
                    return False
        return True