import sys
N,M=map(int, sys.stdin.readline().strip().split())
arr=list(map(int, sys.stdin.readline().strip().split()))
p=[0 for _ in range(N+1)]
p[0]=0
for k in range(1,N+1):
    p[k]=p[k-1]+arr[k-1]
for index in range(M):
    i,j=map(int, sys.stdin.readline().strip().split())
    answer=p[j]-p[i-1]
    print(answer)