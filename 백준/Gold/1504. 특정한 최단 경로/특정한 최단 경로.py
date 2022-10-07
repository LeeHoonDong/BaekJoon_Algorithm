import heapq
import sys
input=sys.stdin.readline
def find_min_distance(graph,start):
    q=[]
    distance=[int(1e9)]*(N+1)
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance
def solution(N,M,arr,v1,v2):
    answer=0
    graph=[[] for _ in range(N+1)]
    for a,b,c in arr:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    distance=find_min_distance(graph,1)
    v1_distance=find_min_distance(graph,v1)
    v2_distance=find_min_distance(graph,v2)
    answer=min(distance[v1]+v1_distance[v2]+v2_distance[N],distance[v2]+v2_distance[v1]+v1_distance[N])
    if answer<int(1e9):
        return answer
    else:
        return -1
# N=4
# M=6
# arr=[[1,2,3],[2,3,3],[3,4,1],[1,3,5],[2,4,5],[1,4,4]]
# v1=2
# v2=3
N,M=map(int,input().split())
arr=[]
for i in range(M):
    arr.append(list(map(int,input().split())))
v1,v2=map(int,input().split())
print(solution(N,M,arr,v1,v2))