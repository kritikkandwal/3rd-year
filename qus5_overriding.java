import java.util.Scanner;
// You are using Java
class Shop {
    //type your code here
    double calculateFinalPrice(double op){
        double dis=op*10/100;
        return op-dis;
    }
    
}

class HolidayShop extends Shop {
    //type your code here
    double calculateFinalPrice(double op){
        double dis=op*10/100;
        double op2=op-dis;
        double dis2=op2*5/100;
        return op2-dis2;
    }
    
}
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double originalPrice = scanner.nextDouble();

        Shop regularShop = new Shop();
        HolidayShop holidayShop = new HolidayShop();

        double regularPrice = regularShop.calculateFinalPrice(originalPrice);
        double holidayPrice = holidayShop.calculateFinalPrice(originalPrice);

        System.out.println("Regular Shop Final Price: " + regularPrice);
        System.out.println("Holiday Shop Final Price: " + holidayPrice);

        scanner.close();
    }
}
