class Solution
{
     public int kthAncestor(Node root, int k, int node)
{
        
     ArrayList<Integer> path= new ArrayList<>();
     int ans = solve(root,path,node);
     if(ans==0 || path.size()<=k) return -1;
     else
     return path.get(k);
        
}
    public int solve(Node root, ArrayList<Integer> path, int node){
    if(root==null) return 0;
    if(root.data==node || solve(root.left,path,node)==1 || solve(root.right,path,node)==1)
{   path.add(root.data);
    return 1;
}
    return 0;
}
}


