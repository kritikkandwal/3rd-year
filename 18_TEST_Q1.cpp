#include<iostream>
using namespace std;

int main()
{
    int n;
    cout<<"ENter size of Array: ";
    cin>>n;

    int arr[n];

    cout<<"Enter values of Array: \n";
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }

    int arr_temp[n];

    for(int i=0; i<n; i++)
    {
        arr_temp[i]=arr[i];
    }

    int temp;

    for(int i=0; i<n; i++)
    {
        for(int j=i+1; j<n; j++)
        {
            if(arr_temp[i]>arr_temp[j])
            {
                temp=arr_temp[j];
                arr_temp[j]=arr_temp[i];
                arr_temp[i]=temp;
            }
        }
    }

    int smallest = arr_temp[0];
    int largest = arr_temp[n-1];

    for(int i=0; i<n; i++)
    {
        if(arr[i]==smallest)
        {
            arr[i]=largest;
        }
        else if(arr[i]==largest)
        {
            arr[i]=smallest;
        }
    }
    
    
    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }


    return 0;
}