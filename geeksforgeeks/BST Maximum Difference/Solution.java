class Solution
{
    int min=Integer.MAX_VALUE;
    int sum=0;
    void find(Node root,int sum)
    {
        if(root==null)
        return;
        if(root.left==null && root.right==null)
        {
            sum+=root.data;
            min=Math.min(min,sum);
        }
        sum+=root.data;
        find(root.left,sum);
        find(root.right,sum);
    }
    Node solve(Node root,int target,int sum)
    {
        if(root==null)
        return null;
        if(root.data==target)
        {
            this.sum=sum;
            return root;
        }
        if(root.data<target)
        return solve(root.right,target,sum+root.data);
        if(root.data>target)
        return solve(root.left,target,sum+root.data);
        return null;
    }
    public int maxDifferenceBST(Node root,int target)
    {
        min=Integer.MAX_VALUE;
        sum=0;
        Node targ=solve(root,target,0);
        if(targ==null)
        return -1;
        find(targ,0);
        return sum-min+target;
        //Please code here
        
    }
}
