import java.util.*;
class qus_5_palindrome{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        String sen=sc.nextLine();
        String rev=new StringBuilder(sen).reverse().toString();

        if(sen.equals(rev)){
            System.out.println("palindrome");
        }
        else{
            System.out.println("Bhag bsdk");
        }
    }
}