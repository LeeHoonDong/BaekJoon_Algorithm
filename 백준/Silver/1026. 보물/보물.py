def solution(N,A,B):
    answer=0
    A.sort()
    B.sort(reverse=True)
    for i in range(N):
        answer+=A[i]*B[i]
    return answer
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(solution(N,A,B))