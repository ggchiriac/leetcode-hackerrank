// https://leetcode.com/problems/add-two-numbers

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        ListNode walk = head;
        
        int remainder = 0;
        while(l1 != null && l2 != null) {
            int sum = l1.val + l2.val + remainder;
            remainder = sum / 10;
            sum = sum % 10;
            ListNode current = new ListNode(sum, null);
            walk.next = current;
            walk = current;
            l1 = l1.next;
            l2 = l2.next;
        }
        while(l1 != null) {
            int sum = l1.val + remainder;
            remainder = sum / 10;
            sum = sum % 10;
            ListNode current = new ListNode(sum, null);
            walk.next = current;
            walk = current;
            l1 = l1.next;
        }
        while(l2 != null) {
            int sum = l2.val + remainder;
            remainder = sum / 10;
            sum = sum % 10;
            ListNode current = new ListNode(sum, null);
            walk.next = current;
            walk = current;
            l2 = l2.next;
        }
        if(remainder != 0) {
            ListNode current = new ListNode(remainder, null);
            walk.next = current;
            walk = current;
        }
        return head.next;
    }
}