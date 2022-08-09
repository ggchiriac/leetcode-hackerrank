// https://leetcode.com/problems/minimum-index-sum-of-two-lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minSum = float('inf')
        hashMap = {}
        choice = []
        for i, place in enumerate(list1):
            hashMap[place] = i
        for i, place in enumerate(list2):
            if place in hashMap:
                if (i + hashMap[place] < minSum):
                    minSum = i + hashMap[place]
                    choice = [place]
                elif (i + hashMap[place] == minSum):
                    choice.append(place)
        return choice
            
        