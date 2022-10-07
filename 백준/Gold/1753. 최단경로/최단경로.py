import heapq
import sys
input=sys.stdin.readline

def dijkstra(graph,visited,distance,start_node):
    visited[start_node]=True
    distance[start_node]=0
    q=[]
    heapq.heappush(q,(0,start_node))
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    for i in range(1,V+1):
        if distance[i]==INF:
            print("INF")
        else:
            print(distance[i])

INF=int(1e9)
V,E=map(int,input().split())
start_node=int(input())
graph=[[] for _ in range(V+1)]
visited=[False]*(V+1)
distance=[INF]*(V+1)
for i in range(E):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost))
dijkstra(graph,visited,distance,start_node)

