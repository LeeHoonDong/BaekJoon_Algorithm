from collections import deque
def BFS(x,y,arr):
    queue=deque()
    queue.append((x,y))
    while queue:
        nx,ny=queue.popleft()
        for index in range(4):
            next_x=nx+dx[index]
            next_y=ny+dy[index]
            if 0<=next_x<N and 0<=next_y<M:
                if arr[next_x][next_y]==1:
                    arr[next_x][next_y]=arr[nx][ny]+1
                    queue.append((next_x,next_y))
    print(arr[N-1][M-1])
dx=[0,0,1,-1]
dy=[1,-1,0,0]
N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input())))
start_x=0
start_y=0
BFS(start_x,start_y,arr)