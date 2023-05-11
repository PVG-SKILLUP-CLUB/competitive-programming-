import math
class Solution:
    def asciisum(self,s,n):
        summ,n =  0,n
        for i in range(1,n):
            summ += abs(ord(s[i])-ord(s[i-1]))
        return summ

    def minimumSum(self, s : str) -> int:
        # code here
        n = len(s)
        s = list(s)
        start, end = 0,n-1
        while start < end:
            if s[start]!='?' and s[end] != '?':
                if s[start] != s[end]:
                    return -1
            elif s[start] == '?' and s[end] == '?':
                if (start > 0):
                    s[start], s[end] = s[start-1], s[start-1]
                else:
                    ele, idx, idx2 = '',1,n-2
                    while idx < idx2:
                        if s[idx] != '?':
                            ele = s[idx]
                            break
                        elif s[idx2] != '?':
                            ele = s[idx2]
                            break
                        idx += 1
                        idx2 -= 1
                    if ele:
                        s[start], s[end] = ele,ele
                    else:
                        s[start], s[end] = 'a','a'
            elif s[start] == '?':
                s[start] = s[end]
            else:
                s[end] = s[start]
            start += 1
            end -= 1
        return self.asciisum(s,n)  
