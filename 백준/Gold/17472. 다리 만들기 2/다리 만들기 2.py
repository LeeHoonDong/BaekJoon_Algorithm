dx=[0,0,1,-1]
dy=[1,-1,0,0]
arr_combi = []
def dfs(arr,i,j,num,maps,N,M):
    if 0>i or 0>j or i>=N or j>=M:
        return False
    if arr[i][j]!=0:
        if maps[i][j]==0:
            maps[i][j]=num
            for index in range(4):
                dfs(arr,i+dx[index],j+dy[index],num,maps,N,M)
            return True
    return False
def make_combination(arr,r,choose,num):
    global arr_combi
    if len(choose)==r:
        arr_combi.append(choose[:])
    for i in range(num,len(arr)):
        make_combination(arr,r,choose+[arr[i]],i+1)
def exists_iland(a,b,ya,yb,maps):
    if a==ya:
        if b<yb:
            for i in range(b+1,yb):
                if maps[a][i]!=0:
                    return True
        elif b==yb:
            return True
        else:
            for i in range(yb+1,b):
                if maps[a][i]!=0:
                    return True
    if b==yb:
        if a < ya:
            for i in range(a + 1, ya):
                if maps[i][b] != 0:
                    return True
        elif a == ya:
            return True
        else:
            for i in range(ya + 1, a):
                if maps[i][b] != 0:
                    return True
    return False
def find_min_distance(edges,maps,N,M,num):
    global arr_combi
    dict_iland={}
    for i in range(N):
        for j in range(M):
            if maps[i][j]!=0:
                if maps[i][j] in dict_iland.keys():
                    dict_iland[maps[i][j]].append([i,j])
                else:
                    dict_iland[maps[i][j]]=[[i,j]]
    #두개의 섬의 거리를 구하는 것이기 때문에
    #조합으로 key에서 두개를 뽑아서
    #해당 배열을 비교하자
    #arr=[1,2,3,4,,,,num]
    arr=[]
    for i in range(1,num+1):
        arr.append(i)
    make_combination(arr,2,[],0)

    for x,y in arr_combi:

        min_distance = int(1e9)
        arr_x=dict_iland[x]
        arr_y=dict_iland[y]
        for a,b in arr_x:
            for ya,yb in arr_y:
                #여기에 추가되어야 할 코드가 (a,b)와 (ya,yb)사이에 섬이 없을때
                if a==ya or b==yb:

                    if exists_iland(a, b, ya, yb, maps)==False:  # 섬이 존재한다면

                        distance=abs(a-ya)+abs(b-yb)-1
                        if distance>1:
                            if distance<min_distance:
                                min_distance=distance
        if min_distance!=int(1e9):
            edges.append((min_distance,x,y))
def find_parent(parent,a):
    if parent[a]!=a:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

if __name__=="__main__":
    arr=[]
    N,M=map(int,input().split())
    maps=[[0 for _ in range(M)]for _ in range(N)]
    edges=[]
    for i in range(N):
       arr.append(list(map(int,input().split())))
    #1. 섬 구분짓기->labeling
    num=1
    for i in range(N):
       for j in range(M):
           if arr[i][j]!=0:
               if dfs(arr,i,j,num,maps,N,M):
                   num+=1
    num-=1#섬의 총 갯수
    #2. 섬들간 최단거리 구하기
    find_min_distance(edges,maps,N,M,num)

    #3. 크루스칼-> 최소 신장 트리
    edges.sort()
    parent=[0 for i in range(num+1)]
    for i in range(num+1):
        parent[i]=i
    answer=0
    count=1
    for cost,x,y in edges:
        if find_parent(parent,x)!=find_parent(parent,y):
            union_parent(parent,x,y)
            answer+=cost
            count+=1

    if answer==0 or count!=num:
        print(-1)
    else:
        print(answer)
