// class qus_1{
//     Node top;

//     static class Node{
//         int data;
//         Node next;

//         Node(int data){
//             this.data=data;
//         }
//     }

//     void push(int x){
//         Node node=new Node(x);
//         node.next=top;
//         top=node;
//     }

//     int  pop(){
//         if(top == null) return-1;
//         int val=top.data;
//         top=top.next;
//         return val;
//     }

//     int peek(){
//         if(top == null) return -1;
//         return  top.data;
//     }

//     boolean boolisEmpty(){
//         return top==null;
//     }

//     public static void main(String[] args) {
//         qus_1 s = new qus_1();

//         s.push(10);
//         s.push(20);
//         s.push(30);
//         s.push(40);
//         s.push(50);
        
//         System.out.println(s.pop());
//         System.out.println(s.peek());
//         System.out.println(s.boolisEmpty());
//     }
// }


import java.util.*;

class qus_1 {
    public static void main(String[] args) {
        Stack<Integer> stack=new Stack<>();
        stack.push(10);
        stack.push(40);
        stack.push(30);
        System.out.println(stack.pop());
        System.out.println(stack.peek());
        System.out.println(stack.size());
        System.out.println(stack.isEmpty());

    }
}

