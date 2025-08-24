import java.util.*;
class first{
    public static void main(String [] args){
    Scanner sc=new Scanner(System.in);

    HashMap<Integer,String> student=new HashMap<>();

    System.out.println("enter number of student");
    int n=sc.nextInt();

    for(int i=0;i<n;i++){
        System.out.print("Enter Roll Number: ");
            int roll = sc.nextInt();
            sc.nextLine(); // consume newline

            System.out.print("Enter Name: ");
            String name = sc.nextLine();

            student.put(roll,name);
    }

    for(HashMap.Entry<Integer,String> entry : student.entrySet()){
        System.out.println(entry.getKey() + "->" + entry.getValue());
    }
    System.out.print("\nEnter roll number to search: ");
    int searchRoll = sc.nextInt();

    if(student.containsKey(searchRoll)){
        System.out.println("Found: " + student.get(searchRoll));
    }
    else {
            System.out.println("Roll number not found.");
        }

    sc.close();
    }
}
