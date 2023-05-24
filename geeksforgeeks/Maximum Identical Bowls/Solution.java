class Solution {
    public static int getMaximum(int N, int[] arr) {
        // code here
        long sum = 0;
        for(int element: arr) sum += element;
        while(sum % N != 0) N--;
        return N;
    }
}
