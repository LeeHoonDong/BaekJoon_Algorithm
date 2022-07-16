def dfs(i,j,N,arr):
    global count
    if i<0 or i>=N or j<0 or j>=N:
        return False
    if arr[i][j]!=0:
        arr[i][j]=0
        
        count+=1
        for index in range(4):
            dfs(i+dx[index],j+dy[index],N,arr)
        return True
    return False

def solution(arr,N):
    global count
    answer=[]
    danji=0
    for i in range(N):
        for j in range(N):
            if arr[i][j]!=0:
                count=0
                if dfs(i,j,N,arr)==True:
                    danji+=1
                    answer.append(count)
    answer.sort()
    answer.insert(0,danji)
    for ele in answer:
        print(ele)

if __name__=="__main__":
    N=int(input())
    arr=[]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    count=0
    for i in range(N):
        arr.append(list(map(int,input())))
    solution(arr,N)