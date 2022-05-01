def BackTracking(depth):
    if len(result)==M:
        print(' '.join(map(str,result)))
        return
    for i in range(1,N+1):
        result.append(i)
        BackTracking(i+1)
        result.pop()
N,M=map(int,input().split())
result=[]
BackTracking(0)