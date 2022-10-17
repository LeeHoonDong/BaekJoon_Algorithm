dx=[0,0,1,-1]
dy=[1,-1,0,0]
from collections import deque

def bfs(maps,N,M,visited):
    q=deque()
    q.append((0,0))
    while q:
        x,y=q.popleft()
        for index in range(4):
            new_x=x+dx[index]
            new_y=y+dy[index]
            if 0<=new_x<N and 0<=new_y<M:
                if maps[new_x][new_y]==1:
                    maps[new_x][new_y]=maps[x][y]+1
                    visited[new_x][new_y]=True
                    q.append((new_x,new_y))
def solution(maps):
    answer = 0
    N=len(maps)
    M=len(maps[0])
    visited=[[False for _ in range(M)] for _ in range(N)]
    bfs(maps,N,M,visited)
    if visited[N-1][M-1]==True:
        answer=maps[N-1][M-1]
    else:
        answer=-1
    return answer