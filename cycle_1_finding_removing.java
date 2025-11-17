class Node {
    int data;
    Node next;

    Node(int val) {
        this.data = val;
        this.next = null;
    }
}

public class cycle_1_finding_removing {

    // Display method safe even if cycle exists
    public static void display(Node head) {
        Node temp = head;
        int count = 0;

        while (temp != null) {
            System.out.print(temp.data + " → ");
            temp = temp.next;
            count++;

            // To avoid infinite printing if cycle exists
            if (count > 15) {
                System.out.println("... (cycle detected while printing)");
                return;
            }
        }
        System.out.println("null");
    }


    // Detect cycle
    public static boolean hasCycle(Node head) {
        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }
        }
        return false;
    }

    // Remove cycle
    public static void removeCycle(Node head) {
        Node slow = head;
        Node fast = head;
        boolean cycleFound = false;

        // Step 1: detect cycle
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                cycleFound = true;
                break;
            }
        }

        if (!cycleFound) return;

        // Step 2: find start of cycle
        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }

        Node start = slow;

        // Step 3: find last node inside cycle
        Node temp = start;
        while (temp.next != start) {
            temp = temp.next;
        }

        // Step 4: break the cycle
        temp.next = null;
    }


    public static void main(String[] args) {

        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        head.next.next.next = new Node(40);
        head.next.next.next.next = new Node(50);

        // Create cycle: 50 → 20
        head.next.next.next.next.next = head.next;

        System.out.println("BEFORE REMOVAL:");
        display(head); // will show limited nodes + cycle warning

        System.out.println(hasCycle(head) ? "Cycle Present" : "No Cycle");

        removeCycle(head);

        System.out.println("\nAFTER REMOVAL:");
        display(head); // now prints clean till null

        System.out.println(hasCycle(head) ? "Cycle Still Present" : "Cycle Removed");
    }
}
