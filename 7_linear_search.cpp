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

    int element;
    cout<<"Enter element: ";
    cin>>element;

    int f=0;
    for(int i=0; i<n; i++)
    {
        if(arr[i]==element)
        {
            f=1;
            break;
        }

    }

    if(f==1)
    {
        cout<<"Element found";
    }
    else{
        cout<<"Element Not found";
    }

    return 0;

}