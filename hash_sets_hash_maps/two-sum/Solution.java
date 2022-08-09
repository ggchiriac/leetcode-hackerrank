// https://leetcode.com/problems/two-sum

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int sum = 0;
        Map<Integer,List<Integer>> indexes = new HashMap();
        for(int i = 0; i < nums.length; ++i) { 
            if(indexes.containsKey(nums[i])) indexes.get(nums[i]).add(i);
            else {
                List<Integer> list = new ArrayList();
                list.add(i);
                indexes.put(nums[i], list);
            }
        }
        
        quickSort(nums, 0, nums.length - 1);
        
        int i = 0, j = nums.length - 1;
        while(i < j) {
            int current = nums[i] + nums[j];
            if(current < target) i++;
            else if(current > target) j--;
                 else {
                     int[] result = new int[2];
                     if(nums[i] == nums[j]) {
                         result[0] = indexes.get(nums[i]).get(0);
                         result[1] = indexes.get(nums[i]).get(1);
                     } else {
                         result[0] = indexes.get(nums[i]).get(0);
                         result[1] = indexes.get(nums[j]).get(0);
                     }
                     return result;
                 }
        }
        return new int[2];
    }
    
    public void quickSort(int[] nums, int start, int end) {
        if(start >= end) return;
        
        int pos = partition(nums, start, end);
        
        quickSort(nums, start, pos - 1);
        quickSort(nums, pos + 1, end);
    }
    
    public int partition(int[] nums, int start, int end) {
        int pivot = nums[end];
        int i = start - 1;
        for(int j = i + 1; j < end; j++) {
            if(nums[j] <= pivot) {
                i++;
                int aux = nums[j];
                nums[j] = nums[i];
                nums[i] = aux;
            }
        }
        int aux = nums[i + 1];
        nums[i + 1] = pivot;
        nums[end] = aux;
        
        return i + 1;
    }
}