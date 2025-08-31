import java.util.*;
class qus1{
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        String[]arr=new String[n];
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLine();
        }

        Map<String,Boolean>wordMap= new HashMap<>();
        for(String i:arr){
            wordMap.put(i,true);
        }
        System.out.print("Enter a word to check: ");
        String searchWord = sc.nextLine();

        if (wordMap.getOrDefault(searchWord, false)) {
            System.out.println("The word '" + searchWord + "' is present.");
        } else {
            System.out.println("The word '" + searchWord + "' is NOT present.");
        }

        

    }
}