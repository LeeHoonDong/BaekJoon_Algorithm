import sys
input=sys.stdin.readline
def solution(N,M,arr):
    answer=0
    dp=[-1 for _ in range(M+1)]
    dp[0]=0
    for i in range(1,M+1):
        for j in range(len(arr)):
            if i>=arr[j]:
                if dp[i-arr[j]]==-1:
                    continue
                dp[i]=max(dp[i],dp[i-arr[j]]+1)
    if dp[M]==0:
        answer=-1
    else:
        answer=dp[M]
    return answer
N,M=map(int,input().split())
arr=list(map(int,input().split()))
print(solution(N,M,arr))