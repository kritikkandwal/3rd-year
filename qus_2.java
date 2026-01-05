// 🔥 INTERVIEW GOLD (MEMORIZE THIS)
// Behavior	    Interface   	Methods

// Queue	    Queue	        offer, poll, peek
// Stack	    Deque	        push, pop, peek
// Avoid	    Stack           class	Legacy

import java.util.*;

class qus_2 {
    public static void main(String[] args) {

        Deque<Integer> dq = new LinkedList<>();

        dq.push(10);
        dq.push(10);
        System.out.println("After push: " + dq);

        dq.pop();
        System.out.println("After pop: " + dq);

        dq.offer(20);
        dq.offer(20);
        System.out.println("After offer: " + dq);

        dq.poll();
        System.out.println("After poll: " + dq);

        System.out.println("Peek: " + dq.peek());
        System.out.println("Size: " + dq.size());
        System.out.println("Is Empty: " + dq.isEmpty());
    }
}
