import java.util.*;

class qus_12_peak {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int arr[] = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // Check the first element
        if (n == 1 || arr[0] >= arr[1]) {
            System.out.println("Peak = " + arr[0]);
            return;
        }

        // Check middle elements
        for (int i = 1; i < n - 1; i++) {
            if (arr[i] >= arr[i - 1] && arr[i] >= arr[i + 1]) {
                System.out.println("Peak = " + arr[i]);
                return;
            }
        }

        // Check last element
        if (arr[n - 1] >= arr[n - 2]) {
            System.out.println("Peak = " + arr[n - 1]);
        }
    }
}
