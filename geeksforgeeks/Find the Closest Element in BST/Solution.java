class Solution
{
    static int minDiff(Node  root, int k) 
    { 
        int minAbsDiff=Integer.MAX_VALUE;            
        int absDiff=0;
        
        while(root!=null){

            if(root.data==k) return 0;
            
            absDiff=Math.abs(root.data-k);
            minAbsDiff=Math.min(minAbsDiff,absDiff);
            
            if(k<root.data){
                root=root.left;
            }else{
                root=root.right;
            }
            
        }
        return minAbsDiff;
    } 
}
