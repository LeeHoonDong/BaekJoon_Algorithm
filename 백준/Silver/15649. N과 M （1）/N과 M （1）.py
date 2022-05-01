def backtracking(answer,visited,depth,M,N):
    if depth==M:
        print(' '.join(map(str,answer)))
        return
    for i in range(1,N+1):
        if visited[i]==False:
            answer.append(i)
            visited[i]=True
            backtracking(answer,visited,depth+1,M,N)
            visited[i]=False
            answer.pop()
def solution(N,M):
    answer=[]
    visited=[False]*(N+1)
    backtracking(answer,visited,0,M,N)

N,M=map(int,input().split())
solution(N,M)
