import sys
input=sys.stdin.readline
arr=[1]*(1000001)
answer=[0]*(1000001)
for j in range(2,1000001):
    k=1
    while j*k<=1000000:
        arr[j*k]+=j
        k+=1
for i in range(1,1000001):
    answer[i]=answer[i-1]+arr[i]
T=int(input())
for i in range(T):
    N=int(input())
    print(answer[N])
    