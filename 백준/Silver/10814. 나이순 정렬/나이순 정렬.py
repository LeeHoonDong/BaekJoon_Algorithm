import sys
input=sys.stdin.readline
N=int(input())
arr=[]
for i in range(N):
    age,name=map(str,input().split())
    age=int(age)
    arr.append([i,age,name])
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])
for a in arr:
    print(a[1],a[2])