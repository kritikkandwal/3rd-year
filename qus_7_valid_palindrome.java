import java.util.*;
class qus_7_valid_palindrome{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String sen=sc.nextLine();
        System.out.println(ispalindrome(sen));
    }

    public static boolean ispalindrome(String sen){
        int left=0;
        int right=sen.length()-1;

        while(left<right){
            while(left<right && !Character.isLetterOrDigit(sen.charAt(left))){
                left++;
            }
            while(left<right && !Character.isLetterOrDigit(sen.charAt(right))){
                right--;
            }

            if(Character.toLowerCase(sen.charAt(left)) != Character.toLowerCase(sen.charAt(right))){
                    return false;
            }
            left++;
            right--;
        }
        return true;
    }
}