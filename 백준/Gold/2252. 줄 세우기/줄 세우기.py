from collections import deque
def topology_sort(graph,indegree):
    answer=[]
    q=deque()
    for i in range(1,len(indegree)):
        if indegree[i]==0:
            q.append(i)
    while q:
        num=q.popleft()
        answer.append(num)
        for i in graph[num]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in answer:
        print(i,end=' ')

n,m=map(int,input().split())
indegree=[0 for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
for i in range(1,m+1):
    A,B=map(int,input().split())
    graph[A].append(B) # A에서 B로 이동 가능
    indegree[B]+=1
topology_sort(graph,indegree)
