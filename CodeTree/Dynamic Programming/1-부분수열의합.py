import sys
input=sys.stdin.readline
def solution(n,m,arr):
    answer=''
    dp=[int(1e9) for _ in range(m+1)]
    dp[0]=0
    for j in range(n):
        for i in range(m,-1,-1):
            if i>=arr[j]:
                dp[i]=min(dp[i],dp[i-arr[j]]+1)
    if dp[m]==int(1e9):
        answer='No'
    else:
        answer='Yes'
    return answer
n,m=map(int,input().split())
arr=list(map(int,input().split()))
print(solution(n,m,arr))
