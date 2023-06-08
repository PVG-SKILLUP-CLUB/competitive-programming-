
class Solution {
    public static long countBits(long N) {
             long count=0;
        for(long i=1;i<=N;i++){
            count+=setBits(i);
        }
        return count;
    }
    public static long setBits(long n){
        long count=0;
        while(n!=0){
            n&=(n-1);
            count++;
        }
        return count;

    }
    }
    //  Brian Kernighan's Algorithm
