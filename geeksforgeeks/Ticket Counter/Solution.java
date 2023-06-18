class Solution {
    public static int distributeTicket(int N,int K)
    {
        int quotient = N/K;
        int remainder = N%K;
        if(quotient%2 == 0){
            return (quotient/2)*K+(remainder == 0 ? 1: remainder);
        }
        else{
            return ((quotient/2)+1)*K+(remainder == 0 ? 0 :1);
        }
    }
}
 
