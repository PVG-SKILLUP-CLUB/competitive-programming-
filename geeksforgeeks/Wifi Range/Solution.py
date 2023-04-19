class Solution:
    def wifiRange(self, N, S, X): 
        prev_high  = -1
        for i in range(N):
            if S[i]=="1":
                temp_high = i+X #farthest right where wifi can reach
                temp_low = i-X #farthest left where wifi can reach
                temp_low = max(temp_low, 0)
                temp_high = min(temp_high, N-1)
                if prev_high+1>=temp_low:   
#previous farthest right point+1 should be more than equal to current lowest
                    prev_high = temp_high   #update high
                else:
                    return False
        if prev_high == N-1:
            return True
        return False
