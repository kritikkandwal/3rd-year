import java.util.*;
class qus_8_remove_adjacent{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a string:");
        String input = sc.nextLine();

        String result = removeDuplicates(input);

        System.out.println("After removing adjacent duplicates: " + result);
    }

    public static String removeDuplicates(String s){
        StringBuilder stack=new StringBuilder();
        for(char ch : s.toCharArray()){

            if (stack.length() > 0 && stack.charAt(stack.length() - 1) == ch) {
                stack.deleteCharAt(stack.length() - 1); // pop
            } 
            else {
                stack.append(ch); // push
            }
        }
        return stack.toString();
    }

}