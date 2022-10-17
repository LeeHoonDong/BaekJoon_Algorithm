def calculate(arr,i,index,jndex):
    #i=4
    #index=1
    #jndex=3라고 가정하면
    #arr[4]에다가 arr[1]과 arr[3]을 계산한 것을 집어넣어야함.
    result=[]
    for ele1 in arr[index]:
        for ele2 in arr[jndex]:
            result.append(ele1+ele2)
            result.append(ele1-ele2)
            result.append(ele1*ele2)
            if ele2!=0:
                result.append(ele1//ele2)
    for ele in result:
        if ele not in arr[i]:
            arr[i].append(ele)
def make_set(arr,i,N):
    arr[i].append(int(str(N)*i))
    for index in range(1,i):
        calculate(arr,i,index,i-index)
def solution(N, number):
    answer = -1
    arr=[[] for _ in range(9)]
    for i in range(1,9):
        make_set(arr,i,N)
        if number in arr[i]:
            answer=i
            break
    return answer