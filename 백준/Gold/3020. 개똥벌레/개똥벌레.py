import sys
input=sys.stdin.readline
N,H=map(int,input().split())
h_jong=[0]*(H+1)
h_suck=[0]*(H+1)
for i in range(N):
    k=int(input())
    if i%2==0:
        h_suck[k]+=1
    else:
        h_jong[k]+=1        
for i in range(H,1,-1):
    h_jong[i-1]+=h_jong[i]
    h_suck[i-1]+=h_suck[i]
for i in range(1,H+1):
    h_jong[i]+=h_suck[H+1-i]
answer=h_jong[1:]
print(min(answer),answer.count(min(answer)))