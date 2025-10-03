#include<iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n;  // Number of students
    cin >> m;  // Number of subjects
    
    int marks[n][m];  // 2D array to store marks for each student
    int sum[n];  // Array to store the sum of marks for each student
    double avg[n];  // Array to store the average for each student
    
    // Take input for all students
    for(int i = 0; i < n; i++) {
        sum[i] = 0;  // Initialize sum for each student
        for(int j = 0; j < m; j++) {
            cin >> marks[i][j];  // Input marks for each subject
            sum[i] += marks[i][j];  // Calculate the sum for the student
        }
        avg[i] = sum[i] / (double)m;  // Calculate average for the student
    }
    
    // Print the sum and average for each student
    for(int i = 0; i < n; i++) {
        cout << "Average for student " << i + 1 << " is: " << avg[i] << endl;
    }
    
    return 0;
}
