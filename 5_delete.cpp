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
    cout<<"\nEnter index to delete: ";
    cin>>index;

    cout<<"\nOriginal Array:  ";

    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<"\t";
    }

    
    for(int i=index; i<n; i++)
    {
        arr[i]=arr[i+1];
    }

    n--;
    
    cout<<"\nNew Array:  \t";

    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<"\t";
    }


    return 0;
}