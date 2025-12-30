import java.util.*;

class qus_11_sqrt {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int sqrt = 0;

        // Normal brute-force method
        for (int i = 1; i * i <= n; i++) {
            sqrt = i;   // store the latest valid i
        }

        System.out.println("Square root (integer part) = " + sqrt);
    }
}
