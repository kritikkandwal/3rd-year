#include<iostream>
using namespace std;

int main()
{
    int n;
    cout<<"Enter n: ";
    cin>>n;

    int arr[n];

    cout<<"Enter values: \n";

    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }

    cout<<"\n";

    cout<<"Original Array:\n";

    for(int i=0; i<n; i++)
    {
        
        cout<<arr[i]<<"\t";
    
        
    }

    cout<<"\n\nSquare of even indexes:  ";
    for(int i=0; i<n; i++)
    {
        if((i+1)%2==0)
        {
            cout<<arr[i]*arr[i]<<"\t";
        }
        
    }

    cout<<"\n";

    cout<<"\nThrice of odd indexes:  ";
    for(int i=0; i<n; i++)
    {
        if((i+1)%2!=0)
        {
            cout<<arr[i]*3<<"\t";
        }
        
    }

    cout<<"\n\n";



    return 0;
}