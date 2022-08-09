// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 1;
        if(s == null || s.length() == 0) return 0;
        String sub = String.valueOf(s.charAt(0));
        for(int i = 1; i < s.length(); i++) {
            if(sub.contains(String.valueOf(s.charAt(i)))) {
                sub = sub.substring(sub.indexOf(s.charAt(i)) + 1);
            } 
            sub += s.charAt(i);
            if(sub.length() > res) res = sub.length();
        }
        return res;
    }
}