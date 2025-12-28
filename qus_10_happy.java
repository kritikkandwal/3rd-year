import java.util.*;
class qus_10_happy{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();

        while(n!=1){
            int sum=0;

            while(n!=0){
                int r=n%10;
                sum=sum+r*r;
                n=n/10;
            }
            n=sum;
        }
        if(n==1){
            System.out.println("happy");
        }
        else{
            System.out.println("nit");
        }
        
    }
        
}