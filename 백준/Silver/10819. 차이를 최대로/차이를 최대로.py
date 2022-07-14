from itertools import permutations
def solution(N,arr):
    answer=0
    list_pers=list(permutations(arr))

    for list_per in list_pers:
        sum=0
        for i in range(len(list_per)-1):
            sum+=abs(list_per[i]-list_per[i+1])
        answer=max(sum,answer)
    return answer

N=int(input())
arr=list(map(int,input().split()))
print(solution(N,arr))