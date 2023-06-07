class Solution
{
   public int[] leastPrimeFactor(int n)
   {
       int a[]=new int[n+1];
       a[1]=1;
       for(int i=2;i<=n;i++)
       {
           for(int j=2;j<=i;j++)
           {
               if(i%j==0)
               {
                   a[i]=j;
                   break;
               }
           }
       }
       return a;
   }
}
