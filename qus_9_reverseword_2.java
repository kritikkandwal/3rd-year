import java.util.*;

public class qus_9_reverseword_2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a sentence:");
        String sentence = sc.nextLine();

        System.out.println("Reverse each word individually:");
        System.out.println(reverseEachWord(sentence));
    }

    public static String reverseEachWord(String sentence) {
        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            result.append(new StringBuilder(word).reverse().toString());
            result.append(" ");
        }

        return result.toString().trim();
    }
}
