// In a company, each manager has a unique employee ID and a monthly salary. You are required to design a program that will calculate and display a manager's annual(12 months) salary based on the user's input details. 



// Implement the solution using a single inheritance approach.



// Employee: The base class with attributes name and employeeID.

// Manager: The derived class inherits from the employee, with an additional attribute salary.

// Input format :
// The input consists of a manager's name (string), employee ID (int) and monthly salary (double) on each line.

// Output format :
// The output prints the manager's name and the calculated annual salary formatted to two decimal places.



// Refer to the sample output for formatting specifications.

// Code constraints :
// The given test cases fall under the following constraints:

// 10,000.0 ≤ monthly salary ≤ 2,00,000.0

// Sample test cases :
// Input 1 :
// Davis
// 234
// 28750.75
// Output 1 :
// Name: Davis
// Annual Salary: Rs. 345009.00
// Input 2 :
// Ramya
// 907
// 37500.25
// Output 2 :
// Name: Ramya
// Annual Salary: Rs. 450003.00
import java.util.Scanner;

// Base class Employee
class Employee {
    String name;
    int employeeID;
}

// Derived class Manager
class Manager extends Employee {
    double salary;

    Manager(String name, int employeeID, double salary) {
        this.name = name;
        this.employeeID = employeeID;
        this.salary = salary;
    }

    // Method to calculate annual salary
    double calculateAnnualSalary() {
        return salary * 12;
    }
}

class qus_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        int employeeID = scanner.nextInt();
        double salary = scanner.nextDouble();

        Manager manager = new Manager(name, employeeID, salary);

        System.out.println("Name: " + manager.name);
        System.out.printf("Annual Salary: Rs. %.2f\n", manager.calculateAnnualSalary());

        scanner.close();
    }
}
