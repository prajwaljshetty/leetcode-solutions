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
    ListNode head;

    public Solution(ListNode head) {
        this.head = head;
    }
    
    public int getRandom() {
        int length = 0;
        ListNode curr;
        Random random = new Random();

        for (curr = head; curr != null; curr = curr.next) {
            length++;
        }

        int target = random.nextInt(length);

        for (curr = head; target > 0; target--) {
            curr = curr.next;
        }

        return curr.val;

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */