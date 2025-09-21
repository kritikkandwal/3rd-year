#include<iostream>
using namespace std;

int main()
{
    int n;
    cout<<"ENter size of Array: ";
    cin>>n;

    int arr1[n],arr2[n];

    cout<<"Enter values of 1st Array: \n";
    for(int i=0; i<n; i++)
    {
        cin>>arr1[i];
    }

    cout<<"Enter values of 2nd Array: \n";
    for(int i=0; i<n; i++)
    {
        cin>>arr2[i];
    }

    int arr_merge[n+n];

    for(int i=0; i<n; i++)
    {
        arr_merge[i]=arr1[i];
    }

    for(int i=0; i<n; i++)
    {
        arr_merge[n+i]=arr2[i];
    }


    int temp;

    for(int i=0; i<n+n; i++)
    {
        for(int j=i+1; j<n+n; j++)
        {
            if(arr_merge[i]>arr_merge[j])
            {
                temp=arr_merge[j];
                arr_merge[j]=arr_merge[i];
                arr_merge[i]=temp;
            }
        }
    }

    int arr_even[n+n];
    int arr_odd[n+n];

    int k=0,l=0;
    for(int i=0; i<n+n; i++)
    {
        if(arr_merge[i] % 2 !=0)
        {
            arr_odd[l++]=arr_merge[i];
        }

        else
        {
            arr_even[k++]=arr_merge[i];
        }
    }

    cout<<"\nAltered Array: ";
    for(int i=0; i<l; i++)
    {
        cout<<arr_odd[i]<<" ";
    }

    for(int i=0; i<k; i++)
    {
        cout<<arr_even[i]<<" ";
    }




    return 0;
}