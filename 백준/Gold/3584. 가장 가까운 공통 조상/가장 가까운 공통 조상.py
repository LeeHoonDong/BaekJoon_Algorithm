import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
def find_parent(x,parent,x_parent):
    if parent[x]!=x:
        x_parent.append(parent[x])
        parent[x]=find_parent(parent[x],parent,x_parent)
    return parent[x]
    
T=int(input())
for i in range(T):
    N=int(input())
    parent=[i for i in range(N+1)]
    for j in range(1,N):
        A,B=map(int,input().split())
        parent[B]=A
    a,b=map(int,input().split())
    a_parent=[]
    b_parent=[]
    a_parent.append(a)
    b_parent.append(b)
    find_parent(a,parent,a_parent)
    find_parent(b,parent,b_parent)
    for num in a_parent:
        if num in b_parent:
            print(num)
            break