class Solution {
    
    public void Rearrange(int arr[], int n)
    {
        int j=0;
        int temp=0;
        for(int i=0; i<n ;i++){
           if(arr[i]<0){
                 int k=i;
                temp=arr[i];
                while(k>j){
                    arr[k]=arr[k-1];
                    k--;
                }
                arr[j]=temp;
                j++;
            }
        }
    }
}
