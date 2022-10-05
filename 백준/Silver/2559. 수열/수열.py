import sys
input=sys.stdin.readline
N,K=map(int,input().split())
arr=list(map(int,input().split()))
answer=[]
answer.append(sum(arr[:K]))
for i in range(N-K):
    answer.append(answer[i]-arr[i]+arr[i+K])
print(max(answer))