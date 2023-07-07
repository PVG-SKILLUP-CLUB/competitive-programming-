class Solution
{
   // arr[]: input array
   // n: size of the array
   //Function to find triplets with zero sum.
public boolean findTriplets(int arr[] , int n)
   {
       //add code here.
       Arrays.sort(arr);
       //boolean ans = false;
       for(int i=0;i<n;i++){
           int left=i+1;
           int right = n-1;
           while(left<right){
               int sum = arr[i]+arr[left]+arr[right];
               if(sum==0){
                   return true;
               }
               else if(sum < 0){
                   left++;
               }
               else{
                   right--;
               }
           }
       }
       return false;
       
       
   }
}
