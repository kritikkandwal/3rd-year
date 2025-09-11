#include<iostream>
using namespace std;

int main()
{
    int n;
    
    cout<<"Enter size of array: ";
    cin>>n;
    
    int arr[n];

    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }


    int index,element;
    cout<<"\nEnter index & element to insert: ";
    cin>>index>>element;

    cout<<"\nOriginal Array:  ";

    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<"\t";
    }

    n++;

    for(int i=n-1; i>=index; i--)
    {
        arr[i+1]=arr[i];
    }

    arr[index]=element;

    
    cout<<"\nNew Array:  \t";

    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<"\t";
    }


    return 0;
}