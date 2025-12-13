import java.util.*;

public class qus_9_reverseword_1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a sentence:");
        String sentence = sc.nextLine();

        System.out.println("Reverse order of words:");
        System.out.println(reverseOrder(sentence));
    }

    public static String reverseOrder(String sentence) {
        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();

        for (int i = words.length - 1; i >= 0; i--) {
            result.append(words[i]);
            result.append(" ");
        }

        return result.toString();
    }
}
