dx=[-1,1,0,0]
dy=[0,0,1,-1]
N=int(input())
graph=[]
count=0
for i in range(N):
    graph.append(list(map(int,input())))
def dfs(i,j):
    global count
    if i<0 or i>=N or j<0 or j>=N:
        return False
    if graph[i][j]==1:
        count+=1
        graph[i][j]=0
        for index in range(4):
            dfs(i+dx[index],j+dy[index])
        return True
    return False 
se=0
arr=[]
for i in range(N):
    for j in range(N):
        if dfs(i,j)==True:
            se+=1
            arr.append(count)
        count=0
print(se)
arr.sort()
for ele in arr:
    print(ele)