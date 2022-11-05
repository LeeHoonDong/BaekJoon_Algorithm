import sys
input=sys.stdin.readline
def solution(N,M,arr):
    answer=0
    #dp 배열 초기화
    dp=[-1 for _ in range(M+1)]
    dp[0]=0
    for w,v in arr:
        for i in range(M,w-1,-1): #뒤로 수행하면 한번씩 사용하는 것을 강제할 수 있음.
            dp[i]=max(dp[i],dp[i-w]+v)
    for ele in dp:
        answer=max(ele,answer)
    return answer
N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

print(solution(N,M,arr))