
class Solution 
{ 
   static long solve(int X,int Y, String S)
    {    
        // code here
          int l=S.length();
        String p = "pr",q = "rp";
        if(Y>X) {
            p="rp";
            q="pr";
            int kl=X;
            X=Y;
            Y=kl;
        }
        int j=l;
        do{
            j=S.length();
            S = S.replaceAll(p,"");
        }while(j!=S.length());
        long x = (l-S.length())/2;
        l=S.length();
        do{
            j=S.length();
            S = S.replaceAll(q,"");
        }while(j!=S.length());
        long y = (l-S.length())/2;
        return x*X + y*Y;
        
    }
}
