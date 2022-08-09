// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        num = {"1", "2", "3", "4", "5", "6"}
        
        def clean(s: str) -> str:
            st = []
            for char in s:
                st.append(char)
                if st[-1] == "0":
                    if len(st) == 1:
                        return "-1"
                    elif st[-2] not in {"1", "2"}:
                        return "-1"
                    else:
                        st.pop()
                        st.pop()
                        st.append("0")
            return ''.join(st)

        @lru_cache(maxsize=None)
        def recurse(s, i) -> int:
            
            if i == 0:
                return 1
            elif i == 1:
                if (s[i-1] == "2" and s[i] in num) or (s[i-1] == "1" and s[i] != "0"):
                    return 2
                else:
                    return 1
            
            if (int(s[i-1]) == 2 and int(s[i]) > 6) or int(s[i-1]) > 2 or s[i] == "0" or int(s[i-1]) == 0:
                return recurse(s, i - 1)
            elif int(s[i-2]) > 2 or int(s[i-2]) == 0:
                return 2 * recurse(s, i - 1)
            else:
                return recurse(s, i - 2) + recurse(s, i - 1)
        
        c = clean(s)
        if c == "-1":
            return 0
        return recurse(c, len(c) - 1)