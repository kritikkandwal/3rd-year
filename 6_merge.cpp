#include<iostream>
using namespace std;

int main()
{
    int arr[5]={1,2,3,4,5};
    int arr2[5]={1,2,3,4,5};

    int arr3[10];

    for(int i=0; i<5; i++)
    {
        arr3[i]=arr[i];
    }

    for(int i=0; i<5; i++)
    {
        arr3[i+5]=arr[i];
    }

    for(int i=0; i<10; i++)
    {
        cout<<arr3[i]<<"\t";
    }

    return 0;
}