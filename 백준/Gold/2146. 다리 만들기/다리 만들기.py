from collections import deque
import sys
sys.setrecursionlimit(1000000)
def dfs(i,j):
    visited[i][j]=True
    arr[i][j]=num
    for index in range(4):
        nx=i+dx[index]
        ny=j+dy[index]
        if 0<=nx<N and 0<=ny<N:
            if visited[nx][ny]==False and arr[nx][ny]==1:
                dfs(nx,ny)
def bfs(arr,num):
    global answer
    queue=deque()
    distance=[[-1]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==num:
                queue.append((i,j))
                distance[i][j]=0
    #큐에다가 group화 된 섬들을 다 넣어준다.
    while queue:
        x,y=queue.popleft()
        for index in range(4):
            nx=x+dx[index]
            ny=y+dy[index]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny]!=0 and arr[nx][ny]!=num:
                    answer=min(answer,distance[x][y])
                    return
                if arr[nx][ny]==0 and distance[nx][ny]==-1:
                    distance[nx][ny]=distance[x][y]+1
                    queue.append((nx,ny))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
visited=[[False]*N for _ in range(N)]
##섬 grouping
num=1#섬의 번호
for i in range(N):
    for j in range(N):
        if visited[i][j]==False and arr[i][j]==1:
            dfs(i,j)
            num+=1
#섬과 섬 사이 가장 짧은 길이 찾기
answer=int(1e9)
for i in range(1,num+1):
    bfs(arr,i)
print(answer)