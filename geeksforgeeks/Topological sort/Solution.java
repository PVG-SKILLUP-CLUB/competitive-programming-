class Solution
{
    //Function to return list containing vertices in Topological order. 
    static int[] topoSort(int V, ArrayList<ArrayList<Integer>> adj) 
    {
        // add your code here
        // Using BFS Algorithm -- (Kahn's Algorithm)
        int[] topo = new int[V];
        int[] indegree = new int[V];
        // calculate the indegree of every vertices
        for(int i=0;i<V;i++){
            for(Integer it : adj.get(i)){
                indegree[it]++;
            }
        }
        Queue<Integer> q = new LinkedList<>();
        // Add element into queue which having indegree Zero
        for(int i=0;i<V;i++){
            if(indegree[i] == 0){
                q.offer(i);
            }
        }
        int ind =0;
        while(!q.isEmpty()){
            Integer node = q.poll();
            topo[ind++] = node;
            for(Integer it : adj.get(node)){
                indegree[it]--;
                if(indegree[it]==0){
                    q.offer(it);
                }
            }
        }
        return topo;
    }
}
