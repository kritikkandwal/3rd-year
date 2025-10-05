#include<iostream>
using namespace std;

int main() {
    int n;
    cout<<"enter size";
    cin >> n;
    int arr[n];
    
    for(int i = 0; i < n; i++) {
        cin >> arr[i]; 
    }
    
    for(int i = 1; i < n; i++) {
        arr[i-1] = arr[i];
    }
    n--;
    
    
    for(int i = 0; i <= n-1; i++) { 
        cout << arr[i] << " ";
    }
    
    return 0;
}