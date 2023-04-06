class Solution{
	int equalSum(int [] A, int N) {
    int totalSum = 0;
    int leftSum = 0;
    

    for (int i = 0; i < N; i++) {
        totalSum += A[i];
    }
    
    for (int i = 0; i < N; i++) {
        if (leftSum == totalSum - leftSum - A[i]) {
            
            return i+1;
        }
        leftSum += A[i];
    }
    
    return -1;
    }
}
