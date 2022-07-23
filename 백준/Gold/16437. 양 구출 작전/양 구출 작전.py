input=__import__('sys').stdin.readline
import sys
sys.setrecursionlimit(1000000)
def dfs(start):
    number_of_sheep=sheeps[start]
    for ele in graph[start]:
        number_of_sheep+=dfs(ele)
    if wolves[start]!=0:#방문한 곳이 늑대가 있다면
        if number_of_sheep>=wolves[start]:#양이 늑대보다 많다면
            number_of_sheep-=wolves[start]
            wolves[start]=0
        else:#늑대가 양보다 많다면 양은 다 잡아먹힘
            wolves[start]-=number_of_sheep
            number_of_sheep=0
    return number_of_sheep

N=int(input())
graph=[[] for _ in range(N+1)]
wolves=[0]*(N+1)
sheeps=[0]*(N+1)

for i in range(2, N+1):
    t,a,p=input().split()
    #graph[i].append(int(p))
    graph[int(p)].append(i)
    if t=='W':
        wolves[i]=int(a)
    else:
        sheeps[i]=int(a)
print(dfs(1))