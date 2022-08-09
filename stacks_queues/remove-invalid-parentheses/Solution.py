// https://leetcode.com/problems/remove-invalid-parentheses

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []

        def countMistakes(s: str) -> List[int]:
            countLeft = 0
            countRight = 0
            for char in s:
                if char == "(":
                    countLeft += 1
                elif char == ")":
                    if countLeft > 0:
                        countLeft -= 1
                    else:
                        countRight += 1
            return [countLeft, countRight]
        
        result = {}
        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)                    
                    result[ans] = 1
            else:
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1,                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)

                expr.append(s[index])    

                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1,
                            left_count,
                            right_count,                            
                            left_rem,
                            right_rem, expr)
                elif s[index] == '(':
                    # Consider an opening bracket.
                    recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)

                # Pop for backtracking.
                expr.pop()                 

        # Now, the left and right variables tell us the number of misplaced left and
        # right parentheses and that greatly helps pruning the recursion.        
        recurse(s, 0, 0, 0, countMistakes(s)[0], countMistakes(s)[1], [])     
        return list(result.keys())