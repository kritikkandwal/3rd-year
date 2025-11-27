import java.util.*;
class qus_3_toggle{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        String result="";
        String sen=sc.nextLine();

        for(int i=0;i<sen.length();i++){
            char ch=sen.charAt(i);
            if(ch>='a' && ch<='z'){
                result=result+(char)(ch-32);
            }
            else if(ch>='A' && ch<='Z'){
                result=result+(char)(ch+32);
            }
            else{
                result=result+ch;
            }
        } 
        System.out.println(result);
    }
}






// import java.util.*;

// class ToggleCaseEasy {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         String s = sc.nextLine();

//         String result = "";

//         for(int i = 0; i < s.length(); i++) {
//             char ch = s.charAt(i);

//             if(Character.isLowerCase(ch)) {
//                 result += Character.toUpperCase(ch);
//             }
//             else if(Character.isUpperCase(ch)) {
//                 result += Character.toLowerCase(ch);
//             }
//             else {
//                 result += ch;  // space, digit, symbol
//             }
//         }

//         System.out.println(result);
//     }
// }

