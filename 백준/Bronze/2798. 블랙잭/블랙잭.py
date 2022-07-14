N,M=map(int,input().split())
card=list(map(int,input().split()))
max_result=0
result=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            result=card[i]+card[j]+card[k]
            if result<=M:
                if max_result<=result:
                    max_result=result
                    
print(max_result)