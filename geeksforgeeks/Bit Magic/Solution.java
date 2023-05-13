class Solution {
    public static int bitMagic(int n, int[] arr) {
         int st=0,end=n-1,count=0;

        while(st<end) 

            if(arr[st++]!=arr[end--])count++;

        return (count+1)/2;
    }
}
