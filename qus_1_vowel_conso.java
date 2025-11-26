import java.util.*;
class qus_1_vowel_conso{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String sen=sc.nextLine();
        int vowel=0;
        int con=0;
        for(int i=0;i<sen.length();i++){
            char ch=sen.charAt(i);

            if((ch>='a' && ch<='z') || (ch>='A' && ch<='Z')){

                if("AEIOUaeiou".indexOf(ch)>=0){
                    vowel++;
                }
                else con++;
            } 
        }
        System.out.println(vowel + "-->"+ con);
    }
}