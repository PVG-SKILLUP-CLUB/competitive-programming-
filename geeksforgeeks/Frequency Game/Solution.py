def LargButMinFreq(arr,n):
    d={}
    m=100000000
    ma=0
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        m=min(d[i],m)
    for i in d:
        if d[i]==m:
            ma=max(ma,i)
    return ma
