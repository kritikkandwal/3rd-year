class Node {
    int data;
    Node next;

    Node(int val) {
        this.data = val;
        this.next = null;
    }
}

public class cycle_3 {

    // Find Nth node from end
    public static Node nthFromEnd(Node head, int n) {

        if (head == null || n <= 0) return null;

        Node slow = head;
        Node fast = head;

        // Step 1: Move fast n steps ahead
        for (int i = 0; i < n; i++) {
            if (fast == null) return null; // n > length
            fast = fast.next;
        }

        // Step 2: Move slow & fast together
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }

        // slow is now at Nth node from end
        return slow;
    }

    public static void main(String[] args) {

        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        head.next.next.next = new Node(40);
        head.next.next.next.next = new Node(50);
        head.next.next.next.next.next = new Node(60);

        int n = 3;

        Node ans = nthFromEnd(head, n);

        if (ans != null)
            System.out.println(n + "th node from end is: " + ans.data);
        else
            System.out.println("Invalid N or list too short");
    }
}
