from itertools import combinations
def solution(N,arr):
    answer=int(1e9)
    group_start=[]
    group_link=[]
    group_num=[i for i in range(N)]
    group=list(combinations(group_num,N//2))
    for i in range(len(group)//2):
        group_start.append(group[i])
        group_link.append(group[len(group)-1-i])

    for i in range(len(group)//2):
        start_score=link_score=0
        start_combi=list(combinations(group_start[i],2))
        link_combi=list(combinations(group_link[i],2))
        for j in range(len(start_combi)):
            start_score+=arr[start_combi[j][0]][start_combi[j][1]]+arr[start_combi[j][1]][start_combi[j][0]]
            link_score+=arr[link_combi[j][0]][link_combi[j][1]]+arr[link_combi[j][1]][link_combi[j][0]]      
        answer=min(answer,abs(start_score-link_score))
    return answer

N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
print(solution(N,arr))