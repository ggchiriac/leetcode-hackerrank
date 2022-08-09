// https://leetcode.com/problems/group-shifted-strings

class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        List<List<String>> result = new ArrayList();
        Map<String, List<String>> map = new HashMap();
        for(int i = 0; i < strings.length; ++i) {
            String key = hash(strings[i]);
            
            if(map.containsKey(key)) map.get(key).add(strings[i]);
            else {
                List<String> list = new ArrayList();
                list.add(strings[i]);
                map.put(key, list);
            }
        }
        
        for(String i : map.keySet()) {
            List<String> current = new ArrayList();
            current.addAll(map.get(i));
            result.add(current);
        }
        return result;
    }
    
    public String hash(String s) {
        char[] letters = s.toCharArray();
        int shift = letters[0];
        for(int i = 0; i < letters.length; ++i) {
            letters[i] = (char) ((letters[i] - shift + 26) % 26 + 'a');
        }
        return String.valueOf(letters);
    }
}