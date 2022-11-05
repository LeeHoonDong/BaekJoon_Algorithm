import sys
input=sys.stdin.readline
def solution(n,arr):
    answer=int(1e9)
    arr=[0]+arr
    dp=[[0 for _ in range(sum(arr)+1)] for _ in range(n+1)]
    dp[0][0]=True
    for i in range(1,n+1):
        for j in range(sum(arr)+1):
            if dp[i-1][j]: #i-1까지의 합이 j일때 i번째에 합이 j가 될때
                dp[i][j]=True
            if j>=arr[i]:
                if dp[i-1][j-arr[i]]: #i-1까지의 합이 j-arr[i]이고 i번째에 합이 j가 될때
                    dp[i][j]=True
    for i in range(1,sum(arr)):
        if dp[n][i]:
            answer=min(answer,abs(i-(sum(arr)-i)))
    return answer
n=int(input())
arr=list(map(int,input().split()))
print(solution(n,arr))