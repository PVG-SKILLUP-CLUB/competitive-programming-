
class Solution
{
    public boolean isWordExist(char[][] board, String word)
    {
        // Code here
        int[][]vis=new int[board.length][board[0].length];
        for(int i=0;i<board.length;i++)
        {
            Arrays.fill(vis[i],-1);
        }
        for(int i=0;i<board.length;i++)
        {
            for(int j=0;j<board[0].length;j++)
            {
                if(board[i][j]==word.charAt(0)&&vis[i][j]==-1)
                {
                    boolean an=dfs(i,j,board,word,1,vis);
                    vis[i][j]=-1;
                    if(an)return true;
                }
            }
        }
        return false;
    }
    boolean dfs(int i,int j,char[][]board,String word,int index,int[][]vis)
    {
        vis[i][j]=1;
        if(index==word.length())return true;
        if(i<board.length-1&&vis[i+1][j]==-1)
        {
          if(board[i+1][j]==word.charAt(index))
          { 
           boolean b=dfs(i+1,j,board,word,index+1,vis);
           vis[i+1][j]=-1;
           if(b)return true;
          }
        }
        if(i>0&&vis[i-1][j]==-1)
        {
            if(board[i-1][j]==word.charAt(index))
            {boolean b1=dfs(i-1,j,board,word,index+1,vis);
            vis[i-1][j]=-1;
            if(b1)return true;}
        }
        if(j<board[0].length-1&&vis[i][j+1]==-1)
        {
            if(board[i][j+1]==word.charAt(index))
            {boolean b2=dfs(i,j+1,board,word,index+1,vis);
            vis[i][j+1]=-1;
            if(b2)return true;}
        }
        if(j>0&&vis[i][j-1]==-1)
        {
            if(board[i][j-1]==word.charAt(index))
            {boolean b3=dfs(i,j-1,board,word,index+1,vis);
            vis[i][j-1]=-1;
            if(b3)return true;}
        }
        return false;
    }
}
