import sys
input=sys.stdin.readline
N,M=map(int,input().split())
answer=0
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
p=[[0 for i in range(N+1)] for j in range(N+1)] 
p[1][1]=arr[0][0]

for i in range(1,N+1):
    for j in range(1,N+1):
        p[i][j]=p[i-1][j]+p[i][j-1]+arr[i-1][j-1]-p[i-1][j-1]

for i in range(M):
    x1,y1,x2,y2=map(int,input().split())
    answer=p[x2][y2]-(p[x1-1][y2]+p[x2][y1-1]-p[x1-1][y1-1])
    print(answer)