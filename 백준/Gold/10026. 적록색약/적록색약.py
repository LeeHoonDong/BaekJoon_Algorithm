from sys import *
setrecursionlimit(10 ** 6)
def change_G_to_R(N,arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='G':
                arr[i][j]='R'

def dfs(i,j,N,visited,arr):
    if visited[i][j]==False:
        visited[i][j]=True
        for index in range(4):
            nx=i+dx[index]
            ny=j+dy[index]
            if (0<=nx<N and 0<=ny<N) and arr[nx][ny]==arr[i][j]:
                dfs(nx,ny,N,visited,arr)
        return True

def solution(N,arr):
    visited=[[False]*N for _ in range(N)]
    three_count=0
    for i in range(N):
        for j in range(N):
            if dfs(i,j,N,visited,arr)==True:
                three_count+=1
    #적록색맹일때 .
    #G를 모두 R로 바꿔준다.     
    visited=[[False]*N for _ in range(N)]       
    two_count=0
    change_G_to_R(N,arr)
    for i in range(N):
        for j in range(N):
            if dfs(i,j,N,visited,arr)==True:
                two_count+=1
    print(three_count, two_count)

N=int(input())
arr=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for i in range(N):
    arr.append(list(map(str,input())))
solution(N,arr)