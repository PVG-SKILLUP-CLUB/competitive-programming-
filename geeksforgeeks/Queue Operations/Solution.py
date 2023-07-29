class Solution:
    
    def insert(self, q, k): 
        q.append(k)
        return q
        
    def findFrequency(self, q, k):
        dict1 = {}
        for i in q:
            if(i not in dict1.keys()):
                dict1[i] = 1
            else:
                dict1[i] += 1
        if(k not in dict1.keys()):
            return 0
        else:
            return dict1[k]
