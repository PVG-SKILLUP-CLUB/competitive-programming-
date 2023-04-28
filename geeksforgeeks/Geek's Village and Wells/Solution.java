class Solution
{
    public class Pair{
        int row;
        int col;
        int val;
        
        Pair(int row, int col, int val){
            this.row=row;
            this.col=col;
            this.val=val;
        }
    }
    
    public int[][] chefAndWells(int n,int m,char c[][])
    {
        //H => MAX
        //W => 0
        //N, . => -1
        
        
        int[][] arr=new int[n][m];
        Queue<Pair> q=new ArrayDeque<>();
        
        
        //create new matrix
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(c[i][j]=='H'){
                    //max
                    arr[i][j]=Integer.MAX_VALUE;
                }
                else if(c[i][j]=='W'){
                    //0
                    arr[i][j]=0;
                    q.add(new Pair(i, j, 0));
                }
                else if(c[i][j]=='.'){
                    //.
                    arr[i][j]=Integer.MAX_VALUE;
                }
                else{
                    //N
                    arr[i][j]=-1;
                }
            }
        }
        
        //bfs
        int[] dx={-1, 0, 0, 1};
        int[] dy={0, -1, 1, 0};
        
        while(q.size()!=0){
            Pair front=q.remove();
            int i=front.row;
            int j=front.col;
            int val=front.val;
            
            //4 dir
            for(int k=0; k<4; k++){
                int newi=i+dx[k];
                int newj=j+dy[k];
                
                if((newi>=0 && newi<n) && (newj>=0 && newj<m) && (arr[newi][newj]!=-1) && (arr[newi][newj]>val+1)){
                    //mark
                    arr[newi][newj]=val+1;
                    //add
                    q.add(new Pair(newi, newj, val+1));
                }
            }
        }
        
        //check
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                
                if(c[i][j]=='.' || c[i][j]=='N'){
                    arr[i][j]=0;
                }
                else if(arr[i][j]==Integer.MAX_VALUE){
                    arr[i][j]=-1;
                }
                else{
                    arr[i][j]=arr[i][j]*2;
                }
            }
        }
        
        return arr;
    }
}
