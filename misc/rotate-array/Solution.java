// https://leetcode.com/problems/rotate-array

class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        if(k == 0) return;
        Map<Integer, Integer> map = new HashMap();
        for(int i = 0; i < n; i++) map.put((i + k) % n, nums[i]);
        for(int i = 0; i < n; i++) nums[i] = map.get(i);
    }
}