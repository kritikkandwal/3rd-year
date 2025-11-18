class Node {
    int data;
    Node next;
    Node(int val) { this.data = val; }
}

public class cycle_2_length  {

    public static int cycleLength(Node head) {
        Node slow = head;
        Node fast = head;

        // Step 1: detect meeting point
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {  // inside cycle
                int count = 1;
                Node temp = slow.next;

                while (temp != slow) {
                    count++;
                    temp = temp.next;
                }

                return count;  // length of cycle
            }
        }
        return 0; // no cycle
    }

    public static void main(String[] args) {

        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        head.next.next.next = new Node(40);
        head.next.next.next.next = new Node(50);
        head.next.next.next.next.next = new Node(50);
        head.next.next.next.next.next.next = new Node(50);

        // Create cycle: 50 → 30
        head.next.next.next.next.next.next.next = head.next.next; 
        

        System.out.println("Cycle length = " + cycleLength(head));
    }
}
