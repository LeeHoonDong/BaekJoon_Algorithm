from collections import deque
def distinct_edge(arr,N,M):
    visited=[[False]*M for _ in range(N)]
    arr[0][0]=-1
    visited[0][0]=True
    queue=deque()
    queue.append((0,0))
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0>ny or ny>=N or 0>nx or nx>=M:
                continue
            if arr[ny][nx]==1 or visited[ny][nx]:
                continue
            arr[ny][nx]=-1
            queue.append((ny,nx))
            visited[ny][nx]=True

def solution(arr,N,M):
    distinct_edge(arr,N,M)#함수의 외부 구분한 것으로 -1
    melt=[]
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                cnt=0
                for index in range(4):
                    nx=j+dx[index]
                    ny=i+dy[index]
                    if nx<0 or nx>=M or ny<0 or ny>=N:
                        continue
                    if arr[ny][nx]==-1:
                        cnt+=1
                    if cnt>=2:
                        melt.append([i,j])
    for j,i in melt:
        arr[j][i]=0

def melt_or_not(arr,N,M):
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                return False
    return True

N,M=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
arr=[]
answer=0
for i in range(N):
    arr.append(list(map(int,input().split())))
while not melt_or_not(arr,N,M):
    answer+=1
    solution(arr,N,M)
print(answer)