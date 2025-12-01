class Node {
    int data;
    Node next;

    Node(int val) {
        this.data = val;
        this.next = null;
    }
}

public class middle_1 {

    public static Node findMiddle(Node head) {
        if (head == null) return null;

        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;      // 1 step
            fast = fast.next.next; // 2 steps
        }

        return slow; // middle
    }

    public static void main(String[] args) {

        // List: 10 -> 20 -> 30 -> 40 -> 50
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        head.next.next.next = new Node(40);
        head.next.next.next.next = new Node(50);

        Node middle = findMiddle(head);
        System.out.println("Middle Node = " + middle.data);
    }
}
