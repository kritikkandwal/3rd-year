// find unique no jo repeat nhi hora ha

// no of array5 
//  1 2 3 1 2
// 3


#include<iostream>
#include <vector>
using namespace std;
int main()
{
    
    int w;
    cout<<"no of array";
    cin>>w;
    vector<int>arr(w);
    for(int i=0;i<w;i++){
        cin>>arr[i];
    }
    int n=arr.size();
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(arr[i]==arr[j]){
                arr[i]=arr[j]=-1;
            }
        }
        if(arr[i]>0){
            cout<<arr[i];
        }
    }
}

