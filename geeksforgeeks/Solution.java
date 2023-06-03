class Solution {
    public static int maxEqualSum(int N1,int N2,int N3, int[] S1, int[] S2, int[] S3) 
   {
        int sum1=0,sum2=0,sum3=0;
        for(int i : S1) sum1+= i;
        for(int i : S2) sum2+= i;
        for(int i : S3) sum3+= i;

        int min = Math.min(sum1, Math.min(sum2,sum3));
        int i=0,j=0,k=0;

        while(i<=N1 && j<=N2 && k<=N3)
        {
            if(sum1>min) sum1-= S1[i++];
            if(sum2>min) sum2-= S2[j++];
            if(sum3>min) sum3-= S3[k++];
            if(sum1==sum2 && sum2==sum3)
                return sum1;
            min = Math.min(sum1, Math.min(sum2,sum3));
        }
        return 0;
    }
}
 
