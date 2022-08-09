// https://leetcode.com/problems/add-binary

class Solution {
    public int toInt(char x) {
        if(x == '0') return 0;
        return 1;
    }
    
    public String addBinary(String a, String b) {
        int la = a.length();
        int lb = b.length();
        int dif = Math.abs(la - lb);
        if (la < lb) for (int i = 0; i < dif; i++) {a = "0" + a; la = lb;}
        if (lb < la) for (int i = 0; i < dif; i++) {b = "0" + b; lb = la;}
        int k = 0;
        String sum = "";
        for (int i = la - 1; i >= 0; i--) {
            int s = k + toInt(a.charAt(i)) + toInt(b.charAt(i));
            if (s == 0) sum = "0" + sum;
            if (s == 1) {
                sum = "1" + sum;
                k = 0;
            }
            if (s == 2) {
                sum = "0" + sum;
                k = 1;
            }
            if (s == 3) {
                sum = "1" + sum;
                k = 1;
            }
        }
        if (k == 1) sum = "1" + sum;
        
        return sum;
    }
}