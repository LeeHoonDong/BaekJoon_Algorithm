from sys import *
setrecursionlimit(10 ** 6)

def dfs(i,j,visited,N):
    if i<0 or i>=N or j<0 or j>=N:
        return False
    if visited[i][j]==1: #물에 안잠겼다면
        visited[i][j]=0 #방문했으니 0으로 
        for index in range(4):
            dfs(i+dx[index],j+dy[index],visited,N)
        return True
    return False
def find_remain_group(visited,N):
    count=0
    for i in range(N):
        for j in range(N):
            if visited[i][j]==1:
                if dfs(i,j,visited,N)==True:
                    count+=1
    return count

def find_height(arr):
    max_height=0
    for line in arr:
        max_height=max(max(line),max_height)
    return max_height
def solution(arr,N):
    answer=0
    #지역 높이의 최댓값을 먼저 구하자.
    max_height=find_height(arr)

    #최소높이부터 최대 높이의 반복문을 수행하면서,
    #해당 높이 이하인 값은 물에 잠기기 때문에 0으로 처리한다.
    #최대 높이-1 까지 반복문을 수행한 이유는
    #최대 높이일때는 전체다 물에 잠기기 때문.
    for height in range(max_height):
        visited=[[1]*N for _ in range(N)] #처음에는 물에 안잠겼기 때문에 1
        for i in range(N):
            for j in range(N):
                if arr[i][j]<=height:
                    visited[i][j]=0 #물에 잠기면 0
        answer=max(find_remain_group(visited,N),answer)
    return answer

N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
print(solution(arr,N))