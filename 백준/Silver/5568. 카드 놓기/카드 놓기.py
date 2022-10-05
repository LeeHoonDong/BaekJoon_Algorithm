from itertools import permutations
import sys
input=sys.stdin.readline
n=int(input())
k=int(input())
arr=[]
answer=[]
for _ in range(n):
    arr.append(input().rstrip())
p_arrs=list(permutations(arr,k))
for p_arr in p_arrs:
    if ''.join(p_arr) not in answer:
        answer.append(''.join(p_arr))
print(len(answer))