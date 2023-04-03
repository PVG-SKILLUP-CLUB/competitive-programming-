class Solution 
{ 
    static int xmod11(String x)
    {    
        // code here
        int s=0;
        for(int i=0;i<x.length();i++)
        {
            s=(s*10+(x.charAt(i)-'0'))%11;
        }
        return s;
    }
} 
