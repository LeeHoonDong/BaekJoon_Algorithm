#벽을 세워, 바이러스가 있는 위치에서 BFS를 수행해서 
#퍼지지 않은 칸의 갯수를 찾아 가장 큰 경우 반환해야하는데
#여기서 문제는 어떻게 벽을 세울것인가?
#Combination??
from itertools import combinations
from collections import deque
def BFS(i,j,visited):
    queue=deque()
    queue.append((i,j))
    while queue:
        nx,ny=queue.popleft()
        visited[nx][ny]=2
        for index in range(4):
            next_x=nx+dx[index]
            next_y=ny+dy[index]
            if 0<=next_x<N and 0<=next_y<M:
                if visited[next_x][next_y]==0:
                    queue.append((next_x,next_y))
def init(arr,visited):
    for i in range(N):
        for j in range(M):
            visited[i][j]=arr[i][j]
def solution(arr,N,M,combi):
    empty_space=0
    visited=[[0]*M for i in range(N)]
    #1로 만들어 3개의 벽 추가로 세웠고
    init(arr,visited)
    for x,y in combi:
        visited[x][y]=1
    #BFS를 통해 바이러스 증식 시켜 안전영역 찾자
    for i in range(N):
        for j in range(M):
            if visited[i][j]==2:
                BFS(i,j,visited)
    #0인 칸의 수 세기
    for i in range(N):
        for j in range(M):
            if visited[i][j]==0:
                empty_space+=1
    return empty_space

dx=[0,0,1,-1]
dy=[1,-1,0,0]
answer=0
N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
empty_space=[]
#빈공간(칸의 값 0) 찾아 집어넣기
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            empty_space.append((i,j))
#조합을 통해 3개 뽑아내기
combis=list(combinations(empty_space,3))
#뽑아낸 것 중 BFS를 통해 최댓값 찾기.
for combi in combis:
    answer=max(answer,solution(arr,N,M,combi))
print(answer)