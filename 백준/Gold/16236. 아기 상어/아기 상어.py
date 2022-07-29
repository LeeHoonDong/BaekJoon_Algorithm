#아기상어 크기 : 2
from collections import deque
def solution(arr):
    queue=deque()
    visited=[[-1]*N for _ in range(N)]
    queue.append((now_x,now_y))
    visited[now_x][now_y]=0
    while queue:
        x,y=queue.popleft()
        for index in range(4):
            nx=x+dx[index]
            ny=y+dy[index]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny]<=now_size and visited[nx][ny]==-1:
                    queue.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
    return visited
def find_size(visited):
    x,y=0,0
    min_distance=int(1e9)
    for i in range(N):
        for j in range(N):
            if visited[i][j]!=-1 and 1<=arr[i][j]<now_size:
                if visited[i][j]<min_distance:
                    x,y=i,j
                    min_distance=visited[i][j]
    if min_distance==int(1e9):
        return None
    else:
        return x,y,min_distance

N=int(input())
dx=[-1,0,1,0]
dy=[0,-1,0,1]
arr=[]
now_size=2
now_x,now_y=0,0
for i in range(N):
    arr.append(list(map(int,input().split())))

#아기상어의 위치 now_x,now_y
for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            arr[i][j]=0 #아기상어가 있는 위치는 거리값이 0
            now_x, now_y=i,j
result=0
cnt=0
while True:
    value=find_size(solution(arr))
    if value==None:#더이상 움직이지 못함 엄마상어의 도움이 필요
        print(result) 
        break
    else:
        now_x,now_y=value[0],value[1]
        result+=value[2]
        arr[now_x][now_y]=0
        cnt+=1
    if cnt>=now_size:
        now_size+=1
        cnt=0
