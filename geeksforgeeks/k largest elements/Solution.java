class Solution {
    int[] kLargest(int[] arr, int n, int k) {
        int sol[]=new int[k];
        Arrays.sort(arr);
        int ind=0;
        for(int x=n-1;x>=n-k;x--)
        {
            sol[ind++]=arr[x];
        }
        return sol;
    }
}
