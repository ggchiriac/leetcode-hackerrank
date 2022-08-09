// https://leetcode.com/problems/first-unique-character-in-a-string

class Solution {
    public int firstUniqChar(String s) {
        Map<Integer, Integer> map = new HashMap(); //key = char, value = index
        for(int i = 0; i < s.length(); ++i) {
            if(map.containsKey(s.charAt(i) - 'a')) map.put(s.charAt(i) - 'a', -1);
            else {
                map.put(s.charAt(i) - 'a', i);
            }
        }
        for(int i = 0; i < s.length(); ++i) {
            if(map.get(s.charAt(i) - 'a') != null && map.get(s.charAt(i) - 'a') != -1) return map.get(s.charAt(i) - 'a');
        }
        return -1;
    }
}