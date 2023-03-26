
class Solution {
  public:
    int unvisitedLeaves(int N, int leaves, int frogs[]) {
        // Code here
        
        vector<bool> visited(leaves+1,false);
        
         for(int i=0;i<N;++i){
             int jump=frogs[i];
             
             if(jump<=leaves && !visited[jump]){
                 
             for(int k=jump;k<=leaves;k+=jump){
                 visited[k]=true;
             }
           }
         }
         
         int cnt=0;
         
         for(int i=1;i<=leaves;++i){
             if(!visited[i]) 
               cnt++;
         }
         
         return cnt;
         
        
    }
};
