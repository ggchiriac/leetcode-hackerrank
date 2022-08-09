// https://leetcode.com/problems/design-linked-list

class MyLinkedList {
    
    public class SinglyListNode {
        int val;
        SinglyListNode next;
        SinglyListNode(int x) { val = x; }
    }
    
    SinglyListNode head;
    int length;
    
    public MyLinkedList() {
        length = 0;
    }
    
    public int get(int index) {
        if (index >= length) return -1;
        SinglyListNode cur = head;
        for(int i = 0; i < index; i++) cur = cur.next;
        return cur.val;
    }
    
    public void addAtHead(int val) {
        SinglyListNode cur = new SinglyListNode(val);
        cur.next = head;
        head = cur;
        length++;
    }
    
    public void addAtTail(int val) {
        if (length == 0) {
            addAtHead(val);
            return;
        }
        SinglyListNode cur = head;
        for(int i = 0; i < length - 1; i++) cur = cur.next;
        SinglyListNode tail = new SinglyListNode(val);
        cur.next = tail;
        length++;
    }
    
    public void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
            return;
        }
        if (index != 0 && index == length) {
            addAtTail(val);
            return;
        }
        if (index > length) return;
        
        SinglyListNode added = new SinglyListNode(val);
        SinglyListNode cur = head;
        for(int i = 0; i < index - 1; i++) cur = cur.next;
        added.next = cur.next;
        cur.next = added;
        length++;
    }
    
    public void deleteAtIndex(int index) {
        if(index >= length) return;
        SinglyListNode cur = head;
        if(index == 0) {
            head = head.next;
            length--;
            return;
        }
        for(int i = 0; i < index - 1; i++) cur = cur.next;
        SinglyListNode after = cur.next;
        cur.next = after.next;
        length--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */