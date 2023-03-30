int minimumInteger(int N, vector<int> &A) {
        
        long long sum = 0;
        long long mini = INT_MAX;
       
        for(int i=0;i<N;i++){
            sum = sum + A[i];
        } 
        
        for(int i=0;i<N;i++){
            
            long long a = A[i];
            
             if(a*N>=sum && a<mini){
                 mini = a;
             }
        } 
        
        return mini;
        
        
    }
