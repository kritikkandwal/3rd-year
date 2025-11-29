import java.util.*;
class qus_2_reverse{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String sen= sc.nextLine();

        StringBuilder sb=new StringBuilder(sen);

        sb.reverse();

        System.out.println(sb.toString());

    }
}