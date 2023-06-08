class Solution {
    public static void fact(int n,int a[])
    {
        a[0]=1;
        for(int i=1;i<=n;i++)
        a[i]=a[i-1]*i;
    }
    public static String kthPermutation(int n,int k) {
        int fact[]=new int[n+1];
        ArrayList<Integer> adj=new ArrayList<>();
        for(int i=1;i<=n;i++)
        adj.add(i);
        fact(n,fact);
        String s1="";
        k-=1;
        while(n!=0)
        {
            s1+=adj.get(k/fact[n-1]);
            adj.remove(k/fact[n-1]);
            k=k%fact[n-1];
            n--;
        }
        return s1;
        // code here
    }
}

