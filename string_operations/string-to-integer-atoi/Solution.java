// https://leetcode.com/problems/string-to-integer-atoi

class Solution {
    public int myAtoi(String s) {
        if(s == null || s.length() == 0) return 0;
        int i = 0;
        int positive = 1;
        int n = s.length();
        while(i < n && s.charAt(i) == ' ') i++;
        
        if(i < n && s.charAt(i) == '-') {
            positive = -1;
            i++;
        } else if(i < n && s.charAt(i) == '+') {
            i++;
        }

        int result = 0;
        while(i < n && s.charAt(i) >= '0' && s.charAt(i) <= '9') {
            int digit = s.charAt(i) - '0';
            
            if(result > Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10 && digit > Integer.MAX_VALUE % 10)) 
                return positive == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            
            result = result * 10 + digit;
            
            i++;
        }
        
        return result * positive;
    }
}