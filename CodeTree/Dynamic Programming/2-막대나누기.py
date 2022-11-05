import sys
input=sys.stdin.readline
def solution(n,arr):
    answer=0
    dp=[-1 for _ in range(n+1)]
    new_arr=[]
    dp[0]=0
    i=1
    for ele in arr:
        new_arr.append([i,ele])
        i+=1
    for length,value in new_arr:
        for i in range(1,n+1):
            if i>=length:
                dp[i]=max(dp[i],dp[i-length]+value)
    answer=dp[n]
    return answer
n=int(input())
arr=list(map(int,input().split()))
print(solution(n,arr))