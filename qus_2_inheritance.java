// Rachael works as a financial advisor and has a client named James who wants to take out a car loan. James provides her with the loan details, including the principal amount, annual interest rate, loan term, and a processing fee associated with the loan. Rachael, being the expert, needs to calculate and provide James with the total interest amount and the total cost of the car loan.

// Write a program that calculates these values based on the provided information. 

// (Use Parent class Loan to calculate interest for a principal amount. Child class CarLoan calculates interest plus an additional processing fee.)

// Input format :
// The first line of input contains a double value representing the principal amount.

// The second line of input contains a double value representing the rate of interest.

// The third line of input contains an integer value representing the number of years.

// The last line of input contains a double value representing the processing charge.

// Output format :
// The output should display as:

// "Total Interest: <<interest>> , interest is the calculated interest and should be rounded to two decimal places.

// Total Cost: <<total>>" , total is the total cost (which would include the principal, interest, and processing charge) and should also be rounded to two decimal places.



// Refer to the sample output for formatting specifications.

// Code constraints :
// 0 ≤ principal ≤1,000,000

// 0 ≤ rateOfInterest ≤100

// 0 ≤ years ≤ 100

// 0 ≤ processingCharge ≤ 100,000

// Sample test cases :
// Input 1 :
// 1000
// 10
// 3
// 500
// Output 1 :
// Total Interest: 300.00
// Total Cost : 800.00
import java.util.Scanner;

class Loan {
    // Base class (can be empty for now)
}

class CarLoan extends Loan {
    double principal;
    double intrate;
    int year;
    double procfee;

    CarLoan(double principal, double intrate, int year, double procfee) {
        this.principal = principal;
        this.intrate = intrate;
        this.year = year;
        this.procfee = procfee;
    }

    double calculateInterest() {
        return (principal * intrate * year) / 100;
    }

    double calculateTotalCost() {
        return calculateInterest() + procfee;
    }
}

class qus_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double principal = scanner.nextDouble();
        double interestRate = scanner.nextDouble();
        int loanTerm = scanner.nextInt();
        double processingFee = scanner.nextDouble();

        CarLoan carLoan = new CarLoan(principal, interestRate, loanTerm, processingFee);

        System.out.printf("Total Interest: %.2f\n", carLoan.calculateInterest());
        System.out.printf("Total Cost: %.2f\n", carLoan.calculateTotalCost());

        scanner.close();
    }
}
