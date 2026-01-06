
// class qus_1_ {

//     // Node definition
//     static class Node {
//         int data;
//         Node next;

//         Node(int data) {
//             this.data = data;
//             this.next = null;
//         }
//     }

//     Node front = null;
//     Node rear = null;

//     // ENQUEUE (insert at rear)
//     void enqueue(int x) {
//         Node newNode = new Node(x);

//         if (rear == null) {
//             front = rear = newNode;
//             System.out.println("Enqueued: " + x + " | Front = " + front.data + ", Rear = " + rear.data);
//             return;
//         }

//         rear.next = newNode;
//         rear = newNode;
//         System.out.println("Enqueued: " + x + " | Front = " + front.data + ", Rear = " + rear.data);
//     }

//     // DEQUEUE (remove from front)
//     int dequeue() {
//         if (front == null) {
//             System.out.println("Queue Underflow");
//             return -1;
//         }

//         int removed = front.data;
//         front = front.next;

//         if (front == null) {
//             rear = null;
//         }

//         System.out.println("Dequeued: " + removed +
//                 " | Front = " + (front != null ? front.data : "null") +
//                 ", Rear = " + (rear != null ? rear.data : "null"));

//         return removed;
//     }

//     // PEEK (front element)
//     int peek() {
//         if (front == null) return -1;
//         return front.data;
//     }

//     // IS EMPTY
//     boolean isEmpty() {
//         return front == null;
//     }

//     // DISPLAY QUEUE
//     void display() {
//         Node temp = front;
//         System.out.print("Queue: ");
//         while (temp != null) {
//             System.out.print(temp.data + " ");
//             temp = temp.next;
//         }
//         System.out.println();
//     }

//     // MAIN METHOD
//     public static void main(String[] args) {

//         qus_1_ q = new qus_1_();

//         q.enqueue(10);
//         q.enqueue(20);
//         q.enqueue(30);

//         q.display();

//         q.dequeue();
//         q.dequeue();

//         q.display();

//         System.out.println("Peek: " + q.peek());
//         System.out.println("Is Empty: " + q.isEmpty());

//         q.dequeue();
//         q.dequeue(); // underflow
//     }
// }


import java.util.*;

class qus_1_ {
    public static void main(String[] args) {

        Queue<Integer> q = new LinkedList<>();

        q.offer(10);
        q.offer(20);
        q.offer(30);

        q.poll();
        q.poll();
    }
}

